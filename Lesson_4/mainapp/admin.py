from django.contrib import admin
from django.contrib.admin import site

from .models import Product

# Register your models here.

admin.site.register(Product)