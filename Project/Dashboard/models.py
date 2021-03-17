from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)
    register = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name