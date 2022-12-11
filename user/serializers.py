from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import user


class userserializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=8)

    class Meta:
        model = user
        fields = ['id', 'name', 'email', 'password']

    def validate(self, attrs):
        email_exists = user.objects.filter(email=attrs['email']).exists
        name_exists = user.objects.filter(name=attrs['name']).exists
        if email_exists:
            raise ValidationError("Email already exists")
        if name_exists:
            raise ValidationError("Username already exists")

        return super().validate(attrs)
