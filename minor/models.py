from django.db import models

# Create your models here.

class Login (models.Model):
    text = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    