from django.conf import settings
from django.db import models


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    product = models.ForeignKey(
        'shop.Product',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    custom_request = models.ForeignKey(
        'services.CustomRequest',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        target = self.product or self.custom_request
        return f'Review {self.rating}/5 by {self.user} on {target}'
