from django.contrib import admin
from .models import Guest, Item, Orders

# Register your models here.

admin.site.register(Guest)
admin.site.register(Item)
admin.site.register(Orders)
