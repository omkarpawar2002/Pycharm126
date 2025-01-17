from django.db import models

# Create your models here.
class User(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=200,primary_key=True)
    password = models.CharField(max_length=40)
