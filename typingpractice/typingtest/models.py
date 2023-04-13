from django.db import models
from django.core.files.storage import default_storage

class MovieScene(models.Model):
    title = models.CharField(max_length=255)
    movie_file = models.FileField(upload_to='movies/')  # Define the movie_file field
    transcript = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
