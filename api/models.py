from django.db import models

# Create your models here.

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=500, blank=False, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    published_at = models.DateTimeField(blank=False, db_index=True)
    thumbnail_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

