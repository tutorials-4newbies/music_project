# Generated by Django 4.0 on 2021-12-20 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs_list', '0004_song_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
    ]
