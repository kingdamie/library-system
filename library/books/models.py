from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField('Author')
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

