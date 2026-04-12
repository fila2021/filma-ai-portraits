from django.urls import path
from . import views


urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('product/<int:product_id>/', views.add_product_review, name='add_product_review'),
    path('request/<int:request_id>/', views.add_custom_request_review, name='add_custom_request_review'),
]