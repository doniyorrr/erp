from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_tovaravet = models.BooleanField(default=False)
