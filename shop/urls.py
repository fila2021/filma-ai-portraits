from django.urls import path

from .views import (
    cart_add,
    cart_checkout,
    cart_clear,
    cart_remove,
    cart_update,
    cart_view,
    cart_add_bundle,
    wishlist_add,
    wishlist_remove,
    wishlist_view,
    wishlist_add_bundle,
    product_detail,
    product_list,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('cart/', cart_view, name='cart_view'),
    path('cart/add/<int:pk>/', cart_add, name='cart_add'),
    path('cart/add-bundle/<int:count>/', cart_add_bundle, name='cart_add_bundle'),
    path('cart/remove/<str:item_key>/', cart_remove, name='cart_remove'),
    path('cart/update/<str:item_key>/', cart_update, name='cart_update'),
    path('cart/clear/', cart_clear, name='cart_clear'),
    path('cart/checkout/', cart_checkout, name='cart_checkout'),
    path('wishlist/', wishlist_view, name='wishlist_view'),
    path('wishlist/add/<int:pk>/', wishlist_add, name='wishlist_add'),
    path('wishlist/add-bundle/<int:count>/', wishlist_add_bundle, name='wishlist_add_bundle'),
    path('wishlist/remove/<str:item_key>/', wishlist_remove, name='wishlist_remove'),
    path('<int:pk>/', product_detail, name='product_detail_by_id'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]
