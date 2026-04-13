from django.urls import path

from .views import activity

urlpatterns = [
    path('activity/', activity, name='account_activity'),
]
