from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
        Serializer for creating a new user.
    """
    class Meta:
        model = User
        fields = ('email', 'password')
