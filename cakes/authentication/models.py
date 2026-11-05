from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your views here.


class RoleChoices(models.TextChoices):

    ADMIN='Admin','Admin'

    USER='User','User'


class Profile(AbstractUser):

    role= models.CharField(max_length=20,choices=RoleChoices)

    class Meta:

        verbose_name='Profiles'

        verbose_name_plural='Profiles'

    def __str__(self):
        
        return self.username