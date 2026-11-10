from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account_module.models import CustomUser
from django.utils.translation import gettext_lazy as _


class UserModelAdmin(UserAdmin):
    model = CustomUser
    list_display = ("first_name", "last_name", "email", "username", "is_active", "is_superuser", "is_staff")
    list_filter = ("is_active", "is_superuser", "is_staff")
    list_editable = ("is_superuser", "is_active")
    searching_fields = ("email", "username")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined", "edited_date")}),
    )
    add_fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password1", "password2"),
            },
        ),
        (
            "Personal Info",
            {
                "fields": ("first_name", "last_name", "username"),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_superuser", "is_staff", "groups",
                    "user_permissions",),
            },
        ),
    )

    readonly_fields = ("last_login", "date_joined", "edited_date")

admin.site.register(CustomUser, UserModelAdmin)