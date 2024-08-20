from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.guest_action, name="guest_action"),
    path("history/", views.AllHistoryViev.as_view(), name="history"),
    path("<int:pk>/choose_item/", views.ChooseItemView.as_view(), name="choose_item"),
    path("<int:pk>/choose_item/ordering/", views.ordering, name="ordering"),
    path("<int:pk>/history/", views.GuestHistoryView.as_view(), name="guest_history"),
    path("<int:pk>/pay/", views.PayView.as_view(), name="pay"),
    path("<int:pk>/pay/paying/", views.paying, name="paying"),
]
