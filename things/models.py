from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    name =models.CharField(
        max_length = 30,
        unique = True,
        blank = False,
        )
    description=models.CharField(
        max_length = 120,
       )
    quantity=models.IntegerField(
    MinValueValidator = 0,
    MaxValueValidator = 100,
    )
