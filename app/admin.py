from django.contrib import admin
from app.models import *
from .models import Product 
# Register your models here.

admin.site.register(Customer)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','price','discounted_price')
    search_fields = ('name', 'category')
    list_filter = ('category',)

