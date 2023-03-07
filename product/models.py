from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Categories(models.Model):
    name_categories = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name_categories
    
class Product(models.Model):
    Product = models.CharField(max_length=120)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    name_categories = models.TextField(blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField()
    image = models.ImageField(upload_to='products', blank=True, null=True)
    def __str__(self):
        return self.Product


# Create your models here.