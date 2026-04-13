from django.contrib import admin
from .models import PromptBundle, PromptSample


@admin.register(PromptBundle)
class PromptBundleAdmin(admin.ModelAdmin):
    list_display = ("label", "count", "price")
    ordering = ("count",)


@admin.register(PromptSample)
class PromptSampleAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order", "id")
