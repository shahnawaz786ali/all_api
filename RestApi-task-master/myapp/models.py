from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    subcategory = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.category_name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

