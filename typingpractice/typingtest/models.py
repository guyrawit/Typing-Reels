from django.db import models

class MovieScene(models.Model):
    title = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=255)
    movie_file = models.FileField(upload_to='movies/')  # Define the movie_file field
    transcript = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title