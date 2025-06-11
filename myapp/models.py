from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name

class Product(models.Model):
    AVAILABILITY_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('preorder', 'Pre-order'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="No description")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='in_stock')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0.0)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"
from django.db import models

# Create your models here.
