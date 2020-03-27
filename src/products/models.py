from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=300) 
    isbn        = models.CharField(max_length=13)
    courses     = models.TextField(blank=True)
    active    = models.BooleanField(default=True) #null=True, 

    def get_absolute_url(self):
    	return reverse("products:product-detail",kwargs = {"id": self.id})