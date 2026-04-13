from django.urls import path

from .views import (
    buy_now,
    cart_checkout_cancel,
    cart_checkout_success,
    order_list,
    order_detail,
    order_receipt,
    order_success,
    order_cancel,
    request_checkout,
    request_checkout_success,
    request_checkout_cancel,
)

urlpatterns = [
    path('buy/<slug:slug>/', buy_now, name='buy_now'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
    path('orders/<int:pk>/receipt/', order_receipt, name='order_receipt'),
    path('orders/<int:pk>/success/', order_success, name='order_success'),
    path('orders/<int:pk>/cancel/', order_cancel, name='order_cancel'),
    path('cart/success/', cart_checkout_success, name='cart_checkout_success'),
    path('cart/cancel/', cart_checkout_cancel, name='cart_checkout_cancel'),
    path('requests/<int:pk>/checkout/', request_checkout, name='request_checkout'),
    path('requests/<int:pk>/success/', request_checkout_success, name='request_checkout_success'),
    path('requests/<int:pk>/cancel/', request_checkout_cancel, name='request_checkout_cancel'),
]
