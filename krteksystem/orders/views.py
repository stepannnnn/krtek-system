from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Guest, Item, Orders
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


# Create your views here.

class IndexView(generic.ListView):
    template_name = "orders/index.html"
    context_object_name = "guest_list"

    def get_queryset(self):
        return Guest.objects.filter(active=True)
    
    

class ChooseItemView(generic.ListView):
    template_name = "orders/choose_item.html"
    context_object_name = "items_list"
    def get_queryset(self):
        return Item.objects.filter(available=True)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['guest'] = Guest.objects.get(pk=self.kwargs['pk'])
        return context

def ordering(request, pk):
    selected_guest = Guest.objects.get(pk=pk)
    selected_item = Item.objects.get(pk=request.POST["item_id"])
    order=Orders(guest=selected_guest, item=selected_item, quantity=1, total=selected_item.price*1, paid=False, time=timezone.now())
    order.save()
    selected_guest.to_pay += selected_item.price
    selected_guest.save()
    context = {"guest": selected_guest, "item": selected_item, "order": order}
    return render(request, "orders/ordering.html", context)



class DetailView(generic.DetailView):
    model = Item
    template_name = "orders/detail.html"

class PayView(generic.ListView):
    template_name = "orders/pay.html"
    context_object_name = "unpaid_history"

    def get_queryset(self):
        self.guest = Guest.objects.get(pk=self.kwargs['pk'])
        return Orders.objects.filter(guest=self.guest, paid=False)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['guest'] = self.guest
        return context
    
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

def paying(request, pk):
    unpaid = Orders.objects.filter(guest=pk, paid=False)
    guest = Guest.objects.get(pk=pk)
    guest.already_paid += guest.to_pay
    guest.to_pay = 0
    for order in unpaid:
        order.paid = True
        order.save()
    guest.save()
    return HttpResponseRedirect(reverse('orders:pay', args=(pk,)))
