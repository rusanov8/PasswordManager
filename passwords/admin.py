from django.contrib import admin

from .models import Password


@admin.register(Password)
class UserAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Password model.
    """
    list_display = ('user', 'service_name')
