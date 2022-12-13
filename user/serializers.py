from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import ValidationError
from .models import user


class userserializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ['id', 'name', 'email', 'password']

    def validate(self, data):
        data = super(userserializer, self).validate(data)

        # debugging #Todo
        print("In the account update validation:")
        print(data)

        return data


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(
        max_length=50,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=50,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def validate(self, data):
        data = super(LoginSerializer, self).validate(data)
        user = authenticate(**data)
        if user:
            return user
        raise AuthenticationFailed
