from django.db import models

from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name=None, last_name=None, password=None):
        if not email:
            raise ValueError("Please provide a valid email address")
        if not username:
            raise ValueError("Please provide a username")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name or "",
            last_name=last_name or "",
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name=None, last_name=None, password=None):
        user = self.create_user(email, username, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin,AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username
    def __str__(self):
        return self.email