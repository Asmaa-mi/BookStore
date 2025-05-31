from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)

from .models import Book, CartItem
admin.site.register(CartItem)

