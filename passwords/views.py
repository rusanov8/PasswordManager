from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as django_filters

from .serializers import PasswordSerializer
from .models import Password
from .filters import PasswordFilterSet


class PasswordRetrieveCreateView(viewsets.ModelViewSet):
    """
        ViewSet for creating and retrieving Password objects.
     """

    serializer_class = PasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
            Get the queryset for the view.
        """
        return Password.objects.filter(user=self.request.user).select_related('user')

    def retrieve(self, request, *args, **kwargs):
        """
            Retrieve a Password object by service name.
        """
        service_name = kwargs.get('service_name').lower()

        try:
            password_instance = Password.objects.select_related('user').get(user=request.user, service_name=service_name)
            serializer = self.get_serializer(password_instance)
            return Response(serializer.data)
        except Password.DoesNotExist:
            return Response({"error": "Password not found for the specified service."}, status=404)


class PasswordListView(generics.ListAPIView):
    """
        List view for Password objects with optional filtering by service name.
    """

    serializer_class = PasswordSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = PasswordFilterSet

    def get_queryset(self):
        """
            Get the queryset for the list view.
        """
        service_name = self.request.query_params.get('service_name')
        queryset = Password.objects.filter(user=self.request.user).prefetch_related('user')

        return queryset
