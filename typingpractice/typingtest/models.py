# from django.db import models
# import os
# from django.core.files.storage import default_storage

# class MovieScene(models.Model):
#     title = models.CharField(max_length=255)
#     movie_name = models.CharField(max_length=255)
#     movie_file = models.FileField(upload_to='movies/')
#     transcript = models.TextField(null=True, blank=True)
#     thumbnail = models.ImageField(upload_to='thumbnail/', null=True)  # Add a thumbnail field
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
import io
import os


from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



import moviepy.editor as mp

class MovieScene(models.Model):
    title = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=255)
    movie_file = models.FileField(upload_to='movies/')
    audio_file = models.FileField(upload_to='audios/')
    transcript = models.TextField(null=True, blank=True)
    transcript_ai = models.TextField(null=True, blank=True)  # Add a new field for the AI-generated transcript
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class UserScore(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
