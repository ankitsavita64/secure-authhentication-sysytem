from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True
    )

    username = models.CharField(
        max_length=100,
        unique=True
    )


    first_name = models.CharField(
        max_length=100,
        blank=True
    )


    last_name = models.CharField(
        max_length=100,
        blank=True
    )


    phone_number = models.CharField(
        max_length=15,
        blank=True
    )


    is_verified = models.BooleanField(
        default=False
    )


    is_active = models.BooleanField(
        default=True
    )


    is_staff = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        default=timezone.now
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "username"
    ]


    def __str__(self):
        return self.email