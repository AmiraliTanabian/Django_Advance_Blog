from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django_jalali.db.models import jDateTimeField
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    """
        Create user with email and password and other fields
        and return the user finally
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Please enter email."))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,password, **extra_fields):
        """
        Create superuser with email and password and other fields
        and return the superuser finally
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(_("For create superuser your should enter is_staff = True"))

        if not extra_fields.get("is_superuser"):
            raise ValueError(_("For create superuser your should enter is_superuser = True"))

        return self.create_user(email=email,password=password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, verbose_name="نام")
    last_name = models.CharField(max_length=255, verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=255, unique=True, verbose_name="ایمیل")
    is_staff = models.BooleanField(default=False, verbose_name="کارمندی")
    is_superuser = models.BooleanField(default=False, verbose_name="کاربر با دسترسی کامل")
    date_joined = jDateTimeField(auto_now_add=True, verbose_name="تاریخ عضویت")
    edited_date = jDateTimeField(auto_now=True, verbose_name="تاریخ تغییر کاربر")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"