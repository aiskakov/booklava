from django.contrib import admin

# Register your models here.
from .models import Product #import Product 

admin.site.register(Product) 