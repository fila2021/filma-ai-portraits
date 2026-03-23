from django.db import models
from django.contrib.auth.models import User


class ServicePackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_images = models.PositiveIntegerField()
    turnaround_days = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CustomRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('tiktok', 'TikTok'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(ServicePackage, on_delete=models.CASCADE)
    platform_type = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    style_choice = models.CharField(max_length=100)
    prompt_details = models.TextField()
    extra_notes = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.package.title}"