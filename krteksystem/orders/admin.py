from django.contrib import admin
from .models import Guest, Item, Orders

# Register your models here.



@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ["pk","name", "to_pay", "already_paid", "active",]
    search_fields = ["name__startswith"]

@admin.register(Item)
class ItemtAdmin(admin.ModelAdmin):
    list_display = ["pk","name", "price", "available"]
    search_fields = ["name__startswith"]

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ["pk","guest", "item", "total", "paid", "time"]
