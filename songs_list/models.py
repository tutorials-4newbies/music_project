from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_year = models.DateField(null=True)
    youtube_link = models.URLField(null=True)
