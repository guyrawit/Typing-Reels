# Generated by Django 4.1.7 on 2023-04-15 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typingtest', '0005_moviescene_movie_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviescene',
            name='movie_audio',
        ),
    ]
