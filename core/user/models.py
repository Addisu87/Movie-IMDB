import uuid
import os

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from core.abstract.models import (AbstractModel, AbstractManager)


def user_image_file_path(instance, filename):
    """
    Generate file path for new user image.
    """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('user', filename)


class UserManager(BaseUserManager, AbstractManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_kwargs):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address.")

        if not password:
            raise ValueError("Users must have a password.")

        user = self.model(email=self.normalize_email(email), **extra_kwargs)
        # hashing password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_kwargs):
        """
        Create and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password, **extra_kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractModel, AbstractBaseUser):
    """User in the system."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(db_index=True, max_length=50, unique=True)
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True)
    avatar = models.ImageField(null=True, upload_to=user_image_file_path)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, movies):
        "Does the user have permissions to view the app `movies`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
