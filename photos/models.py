from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    s3_key = models.CharField(max_length=500)
    s3_url = models.URLField(max_length=1000)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title

