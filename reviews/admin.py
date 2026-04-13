from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "custom_request", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = (
        "comment",
        "user__username",
        "user__email",
        "product__title",
        "custom_request__id",
    )
    ordering = ("-created_at",)
