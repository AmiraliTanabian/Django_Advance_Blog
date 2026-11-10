from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account_module.models import CustomUser, UserProfile
from django.utils.translation import gettext_lazy as _


class UserModelAdmin(UserAdmin):
    model = CustomUser
    list_display = ( "email", "username", "is_active", "is_superuser", "is_staff")
    list_filter = ("is_active", "is_superuser", "is_staff")
    list_editable = ("is_superuser", "is_active")
    searching_fields = ("email", "username")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
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
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password1", "password2"),
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

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name")
    search_fields = ("user__email", "first_name", "last_name")
    ordering = ("user__email",)


admin.site.register(CustomUser, UserModelAdmin)
admin.site.register(UserProfile, ProfileAdmin)