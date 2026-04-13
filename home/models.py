from django.db import models


class PromptBundle(models.Model):
    label = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    class Meta:
        ordering = ['count']

    def __str__(self):
        return f"{self.label} ({self.count})"


class PromptSample(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title
