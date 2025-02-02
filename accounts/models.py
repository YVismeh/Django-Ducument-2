from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id_code = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=14, unique=True)
    image = models.ImageField(upload_to="user", default="default.jpg")

    def __str__(self):
        return self.username
    
