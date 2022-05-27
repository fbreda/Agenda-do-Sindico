from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    condo = models.CharField(blank=True, max_length=120)
    birthday = models.CharField(blank=True, max_length=20)
    celular = models.CharField(blank=True, max_length=120)
