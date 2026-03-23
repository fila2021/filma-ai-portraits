from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    category = models.CharField(max_length=100, blank=True)
    caption = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title