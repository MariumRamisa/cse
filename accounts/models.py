from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.


class AuthProvider(models.Model):
    auth_provider = models.CharField(
        max_length=30, unique=True, primary_key=True,
        blank=False, null=False)

    objects = models.Manager()


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email',
                              max_length=100, unique=True)  # ,db_index=True)
    username = models.CharField(verbose_name='username', max_length=50)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    is_first_login = models.BooleanField(
        verbose_name='first_login', default=True)

    auth_provider = models.ForeignKey(AuthProvider, on_delete=models.PROTECT)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def has_auth_provider(self, authProvider):
        return Account.get_accounts_from_auth_provider(authProvider).filter(pk=self.pk).exists()

    @staticmethod
    def get_accounts_from_auth_provider(authProvider):
        authProvider = AuthProvider.objects.get(pk=authProvider)
        return Account.objects.filter(auth_provider=authProvider)
