from django.urls import path

from .views import (
    cart_add,
    cart_checkout,
    cart_remove,
    cart_view,
    product_detail,
    product_list,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('cart/', cart_view, name='cart_view'),
    path('cart/add/<int:pk>/', cart_add, name='cart_add'),
    path('cart/remove/<str:item_key>/', cart_remove, name='cart_remove'),
    path('cart/checkout/', cart_checkout, name='cart_checkout'),
    path('<int:pk>/', product_detail, name='product_detail_by_id'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]