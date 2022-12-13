from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import Account, AuthProvider


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'username', 'is_first_login',
                  'profile_type', 'profile_image']
        extra_kwargs = {
            'email': {'read_only': True},
            'is_first_login': {'read_only': True},
            'profile_type': {'read_only': True},
        }

    def validate(self, data):
        data = super(AccountSerializer, self).validate(data)

        # debugging #Todo
        print("In the account update validation:")
        print(data)

        return data


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def validate(self, data):
        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match', 'password2': 'Passwords must match'})
        return data

    def save(self):
        account = Account.objects.create_account(email=self.validated_data['email'],
                                                 username=self.validated_data['username'],
                                                 password=self.validated_data['password'])
        return account


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise AuthenticationFailed


class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    new_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    new_password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        data = super(PasswordSerializer, self).validate(data)

        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError(
                {"old_password": "Wrong Password"})
        elif data['new_password'] != data['new_password']:
            raise serializers.ValidationError(
                {"new_password": "Passwords don't match", "new_password2": "Passwords don't match"})
        return data


class ConfigureProfileSerializer(serializers.ModelSerializer):

    profile_type = serializers.CharField(required=True, allow_blank=False)

    class Meta:
        model = Account
        fields = ['is_first_login']
        extra_kwargs = {
            'is_first_login': {'write_only': True},

        }

    def validate(self, data):
        if data.get('profile_image') is None and data['profile_type'] == 'Student':
            raise serializers.ValidationError(
                {"profile_image": "You must provide a profile picture"})
        data['profile_type'] = ProfileType.objects.get(pk=data['profile_type'])
        return data
