from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    name = models.CharField(max_length=30)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.email


