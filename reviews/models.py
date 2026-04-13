from django.conf import settings
from django.db import models

from services.models import CustomRequest
from shop.models import Product


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
    )
    custom_request = models.ForeignKey(
        CustomRequest,
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        target = self.product or self.custom_request
        target_label = f" for {target}" if target else ""
        return f"Review by {self.user}{target_label} ({self.rating}/5)"
