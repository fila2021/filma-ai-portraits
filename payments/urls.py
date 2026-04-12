from django.urls import path

from .views import (
    buy_now,
    order_detail,
    request_checkout,
    request_checkout_success,
    request_checkout_cancel,
)

urlpatterns = [
    path('buy/<slug:slug>/', buy_now, name='buy_now'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
    path('requests/<int:pk>/checkout/', request_checkout, name='request_checkout'),
    path('requests/<int:pk>/success/', request_checkout_success, name='request_checkout_success'),
    path('requests/<int:pk>/cancel/', request_checkout_cancel, name='request_checkout_cancel'),
]
