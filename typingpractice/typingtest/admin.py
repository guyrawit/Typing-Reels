from django.contrib import admin
from .models import MovieScene
from .utils import generate_transcript_ai

def run_generate_transcript_ai(modeladmin, request, queryset):
    for movie_scene in queryset:
        generate_transcript_ai(movie_scene)

run_generate_transcript_ai.short_description = 'Generate transcript AI'

@admin.register(MovieScene)
class MovieSceneAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie_name', 'audio_file', 'movie_file', 'transcript', 'transcript_ai', 'created_at')
    actions = [run_generate_transcript_ai]
