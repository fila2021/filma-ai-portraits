from django.urls import path
from .views import product_detail, product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail_by_id'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]