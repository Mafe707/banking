from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.abrev} {'Activate' if self.status else 'Inactive'}"

class Departments(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    id_countries = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='departments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Cities(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    id_departments = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='cities')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile_phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=True)
    id_cities = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    
class Department(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
