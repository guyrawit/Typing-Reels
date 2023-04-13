from django.contrib import admin
from .models import MovieScene

class MovieSceneAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    # Add the 'movie_file' field to the form for file upload
    fieldsets = (
        (None, {'fields': ('title', 'movie_file', 'transcript')}),
    )

admin.site.register(MovieScene, MovieSceneAdmin)
