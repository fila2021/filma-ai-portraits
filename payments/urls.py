from django.urls import path

from .views import buy_now, order_detail

urlpatterns = [
    path('buy/<slug:slug>/', buy_now, name='buy_now'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
]
