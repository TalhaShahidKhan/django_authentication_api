from django.db import models
from django.contrib.auth.models import AbstractUser
from account.manager import CustomUserManager


class CustomUser(AbstractUser):
    email = models.CharField(unique=True, max_length=255)
    tc = models.BooleanField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    