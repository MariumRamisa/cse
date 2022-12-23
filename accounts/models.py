
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
"""
