from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserAdminE(UserAdmin):
    list_display = ["username", "email", "first_name", "last_login", "is_staff", "is_superuser"]

admin.site.unregister(User)
admin.site.register(User, UserAdminE)