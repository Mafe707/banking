from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    
class Department(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
