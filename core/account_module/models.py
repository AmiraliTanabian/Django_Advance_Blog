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
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")
    objects = UserManager()

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="user-profiles", blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    date_joined = jDateTimeField(auto_now_add=True)
    edited_date = jDateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

