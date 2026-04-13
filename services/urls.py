from django.urls import path
from .views import (
    create_request,
    delete_request,
    edit_request,
    request_detail,
    request_success,
    request_list,
    service_list,
    service_detail,
)

urlpatterns = [
    path('', service_list, name='service_list'),
    path('<int:pk>/', service_detail, name='service_detail'),
    path('requests/', request_list, name='request_list'),
    path('requests/create/', create_request, name='create_request'),
    path('requests/<int:pk>/success/', request_success, name='request_success'),
    path('requests/<int:pk>/', request_detail, name='request_detail'),
    path('requests/<int:pk>/edit/', edit_request, name='edit_request'),
    path('requests/<int:pk>/delete/', delete_request, name='delete_request'),
]
