from django.urls import path
from .views import edit_profile, profile_detail, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile_detail, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]