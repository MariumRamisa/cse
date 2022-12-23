from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeform(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('email',)
