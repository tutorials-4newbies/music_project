from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_year = models.DateField(null=True)
    youtube_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
