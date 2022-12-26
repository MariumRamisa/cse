
"""from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationform, CustomUserChangeform

# Register your models here.


# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationform
    form = CustomUserChangeform
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    add_fieldsets = (
        (None, {
         'classes': ('wide'),
         'fields': ('email', 'password', 'password2', 'is_staff', 'is_active')
         }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
"""
