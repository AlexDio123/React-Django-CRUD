from xml.etree.ElementTree import fromstring
from django.contrib import admin
from .models import Category

# Register your models here.

admin.site.register(Category)