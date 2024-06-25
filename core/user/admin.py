from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
        ("Important dates", {'fields': ['last_login']}),
        ('Personal Info', {'fields': [
         'first_name', 'last_name', 'username', 'avatar']}),
    ]
    readonly_fields = ['last_login']

    add_fieldsets = [
        (None, {
            "classes": ["wide"],
            'fields': [
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'username',
                'avatar',
                'is_active',
                'is_staff',
                'is_superuser'
            ]
        }),
    ]

    filter_horizontal = []
    list_filter = ['is_active', 'is_staff', 'is_superuser']


# Register the new UserAdmin
admin.site.register(User, UserAdmin)
