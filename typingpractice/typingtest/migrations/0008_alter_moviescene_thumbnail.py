# Generated by Django 4.1.7 on 2023-04-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typingtest', '0007_moviescene_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviescene',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnail/'),
        ),
    ]
