from django.contrib import admin
from django.urls import path, include

from home.views import home, about, browse

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('browse/', browse, name='browse'),

    path('accounts/', include('accounts.urls')),
    path('account/', include('account.urls')),
    path('gallery/', include('gallery.urls')),
    path('shop/', include('shop.urls')),
    path('services/', include('services.urls')),
    path('payments/', include('payments.urls')),
    path('reviews/', include('reviews.urls')),
]
