from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name =models.CharField(
        max_length = 30,
        unique = True,
        blank = False,
        )
    description=models.CharField(
        max_length = 120,
       )
    quantity=models.IntegerField(
       validators = [MaxValueValidator(100),MinValueValidator(1)] 
    )
    #Required field
    REQUIRED_FIELDS = ['name','description','quantity']
    