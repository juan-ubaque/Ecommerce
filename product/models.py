from django.db import models

class Product(models.Model):
    Product = models.CharField(max_length=120)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    name_categories = models.TextField(blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField()
    image = models.ImageField(upload_to='products', blank=True, null=True)
    def __str__(self):
        return self.Product

class Categories(models.Model):
    name_categories = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name_categories
# Create your models here.