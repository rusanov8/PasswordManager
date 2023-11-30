from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
        Admin configuration for the User model.
    """
    list_display = ('email',)
    search_fields = ('email',)
