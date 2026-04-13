from django.conf import settings
from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey('shop.Product', on_delete=models.PROTECT, related_name='orders', null=True, blank=True)
    bundle_label = models.CharField(max_length=150, blank=True)
    bundle_count = models.PositiveIntegerField(null=True, blank=True)
    price_snapshot = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_session_id = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        label = self.product.title if self.product else (self.bundle_label or 'Bundle')
        return f'Order #{self.pk} - {label}'


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('succeeded', 'Succeeded'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    order = models.ForeignKey('payments.Order', on_delete=models.CASCADE, null=True, blank=True, related_name='payments')
    custom_request = models.ForeignKey('services.CustomRequest', on_delete=models.CASCADE, null=True, blank=True, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=10, default='eur')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    stripe_payment_intent = models.CharField(max_length=255, blank=True)
    stripe_session_id = models.CharField(max_length=255, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        target = self.order or self.custom_request
        return f'Payment {self.status} - {target}'
