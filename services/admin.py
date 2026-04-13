from django.contrib import admin
from django.utils.html import format_html

from .models import CustomRequest, ServicePackage


@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform_type', 'base_price', 'number_of_images', 'turnaround_days', 'is_active', 'image_link')
    list_filter = ('platform_type', 'is_active')
    search_fields = ('name',)

    @staticmethod
    def image_link(obj):
        if obj.image_url:
            return format_html('<a href="{}" target="_blank" rel="noopener">Open</a>', obj.image_url)
        return '—'
    image_link.short_description = "Image"


@admin.register(CustomRequest)
class CustomRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'package', 'platform_type', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'platform_type')
    search_fields = ('user__username', 'package__name')
