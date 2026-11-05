from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_jalali.db.models import jDateTimeField

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, verbose_name="نام")
    last_name = models.CharField(max_length=255, verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=255, unique=True, verbose_name="ایمیل")
    is_staff = models.BooleanField(default=False, verbose_name="کارمندی")
    is_superuser = models.BooleanField(default=False, verbose_name="کاربر با دسترسی کامل")
    date_joined = jDateTimeField(auto_now_add=True, verbose_name="تاریخ عضویت")
    edited_date = jDateTimeField(auto_now=True, verbose_name="تاریخ تغییر کاربر")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name", "email")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"