from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.username
