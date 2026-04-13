from django.conf import settings
from django.db import models


class ServicePackage(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('tiktok', 'TikTok'),
        ('youtube', 'YouTube'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    number_of_images = models.PositiveIntegerField(default=10)
    turnaround_days = models.PositiveIntegerField(default=3)
    platform_type = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CustomRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    STYLE_CHOICES = [
        ('realistic', 'Realistic'),
        ('cartoon', 'Cartoon'),
        ('cinematic', 'Cinematic'),
        ('studio', 'Studio'),
        ('other', 'Other'),
    ]

    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('tiktok', 'TikTok'),
        ('youtube', 'YouTube'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='custom_requests'
    )
    package = models.ForeignKey(
        ServicePackage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='requests'
    )
    platform_type = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    style_choice = models.CharField(max_length=20, choices=STYLE_CHOICES)
    prompt_details = models.TextField()
    extra_notes = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Request #{self.pk} - {self.user.username}"

    def save(self, *args, **kwargs):
        if self.package and (not self.total_price or self.total_price == 0):
            self.total_price = self.package.base_price
        super().save(*args, **kwargs)
