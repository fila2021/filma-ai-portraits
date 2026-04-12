from django.urls import path

from .views import (
    create_product_review,
    create_request_review,
    delete_review,
    edit_review,
)

urlpatterns = [
    path('products/<slug:slug>/add/', create_product_review, name='create_product_review'),
    path('requests/<int:pk>/add/', create_request_review, name='create_request_review'),
    path('<int:pk>/edit/', edit_review, name='edit_review'),
    path('<int:pk>/delete/', delete_review, name='delete_review'),
]
