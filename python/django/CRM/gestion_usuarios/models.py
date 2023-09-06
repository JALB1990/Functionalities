from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=16)
    password = models.BinaryField()
    email = models.EmailField()

