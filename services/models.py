from django.db import models


class ServicePackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_images = models.PositiveIntegerField()
    turnaround_days = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title