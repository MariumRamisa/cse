from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import user


class userserializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ['id', 'name', 'email', 'password']

   # def validate(self, attrs):
     #  email_exists = user.objects.filter(email=attrs['email']).exists
      #  name_exists = user.objects.filter(name=attrs['name']).exists
      #  if email_exists:
      #      raise ValidationError("Email already exists")
       # elif name_exists:
       #     raise ValidationError("Username already exists")
#
      #  return super().validate(attrs)
