from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Guest, Item, Orders

# Create your views here.

class IndexView(generic.ListView):
    model = Guest
    template_name = "orders/index.html"
    context_object_name = "guest_list"

    

class ChooseItemView(generic.ListView):
    model = Item
    template_name = "orders/choose_item.html"
    context_object_name = "items_list"


class DetailView(generic.DetailView):
    model = Item
    template_name = "orders/detail.html"

class PayView(generic.ListView):
    template_name = "orders/pay.html"
    context_object_name = "unpaid_history"

    def get_queryset(self):
        self.guest = Guest.objects.get(pk=self.kwargs['pk'])
        return Orders.objects.filter(guest=self.guest, paid=False)
    
class GuestHistoryView(generic.ListView):
    template_name = "orders/guest_history.html"
    context_object_name = "guest_history"

    def get_queryset(self):
        self.guest = Guest.objects.get(pk=self.kwargs['pk'])
        return Orders.objects.filter(guest=self.guest)
    
class AllHistoryViev(generic.ListView):
    template_name = "orders/all_history.html"
    context_object_name = "all_history"

    def get_queryset(self):
        return Orders.objects.order_by('time')

        
    