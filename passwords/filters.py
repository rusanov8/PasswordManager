from django_filters import CharFilter, FilterSet
from .models import Password


class PasswordFilterSet(FilterSet):
    """
        FilterSet for the Password model.
    """

    service_name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Password
        fields = ('service_name',)
