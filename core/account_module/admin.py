from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account_module.models import CustomUser
from django.utils.translation import gettext_lazy as _


class UserModelAdmin(UserAdmin):
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
    readonly_fields = ("last_login", "date_joined", "edited_date")

admin.site.register(CustomUser, UserModelAdmin)