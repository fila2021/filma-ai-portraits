from django.contrib import admin

from .models import CustomRequest, ServicePackage


@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform_type', 'base_price', 'number_of_images', 'turnaround_days', 'is_active')
    list_filter = ('platform_type', 'is_active')
    search_fields = ('name',)


@admin.register(CustomRequest)
class CustomRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'package', 'platform_type', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'platform_type')
    search_fields = ('user__username', 'package__name')
