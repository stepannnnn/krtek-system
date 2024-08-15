from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField()

    def __str__(self):
        return self.name


class Guest(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField()

    class Meta:
        ordering = ["name"]    

    def __str__(self):
        return self.name
    

    
class Orders(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField()
    time = models.DateTimeField("time of adding")

    def __str__(self):
        return f'{self.guest.name} ordered {self.quantity} {self.item.name}'
    
