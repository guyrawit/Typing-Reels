from django.db import models
import os
from django.core.files.storage import default_storage

class MovieScene(models.Model):
    title = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=255)
    movie_file = models.FileField(upload_to='movies/')
    transcript = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True)  # Add a thumbnail field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class UserScore(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
