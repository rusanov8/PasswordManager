from rest_framework import serializers
import base64
from .models import Password


class PasswordSerializer(serializers.ModelSerializer):
    """
        Serializer for the Password model.
    """

    class Meta:
        model = Password
        fields = ('password', 'service_name')
        read_only_fields = ('service_name',)

    def create(self, validated_data):
        """
            Create method for the serializer.
            If a password for the specified user and service exists, update the password.
            Otherwise, create a new password entry.
        """
        user = self.context['request'].user
        service_name = self.context['request'].parser_context['kwargs'].get('service_name').lower()

        password_object = Password.objects.filter(user=user, service_name=service_name).first()

        if password_object:
            password_object.password = base64.b64encode(validated_data['password'].encode())
            password_object.save()
            print(password_object.password)
        else:
            validated_data['user'] = user
            validated_data['service_name'] = service_name
            validated_data['password'] = base64.b64encode(validated_data['password'].encode())
            password_object = Password.objects.create(**validated_data)

        return password_object

    def to_representation(self, instance):
        """
            Convert the password from base64 encoding to plain text in the representation.
        """
        print(base64.b64decode(instance.password))
        instance.password = base64.b64decode(instance.password).decode()
        return super().to_representation(instance)







