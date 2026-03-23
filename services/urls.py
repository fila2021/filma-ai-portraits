from django.urls import path
from .views import (
    create_request,
    delete_request,
    edit_request,
    request_detail,
    request_list,
    service_list,
)

urlpatterns = [
    path('', service_list, name='service_list'),
    path('requests/', request_list, name='request_list'),
    path('requests/create/', create_request, name='create_request'),
    path('requests/<int:pk>/', request_detail, name='request_detail'),
    path('requests/<int:pk>/edit/', edit_request, name='edit_request'),
    path('requests/<int:pk>/delete/', delete_request, name='delete_request'),
]