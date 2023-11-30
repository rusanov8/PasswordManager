from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User
from .serializers import UserCreateSerializer



class UserCreateApiView(generics.CreateAPIView):
    """
        API view for user creation.
    """
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        User.objects.create_user(**serializer.validated_data)




