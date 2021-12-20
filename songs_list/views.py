from django.shortcuts import render

from songs_list.models import Song, Artist


def index(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()
    context = {
        "songs": songs,
        "artists": artists
    }
    return render(request, 'songslist/index.html', context)
