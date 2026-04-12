from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from home.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('gallery/', include('gallery.urls')),
    path('shop/', include('shop.urls')),
    path('services/', include('services.urls')),
    path('payments/', include('payments.urls')),
    path('reviews/', include('reviews.urls')),
]
