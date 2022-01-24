from django.shortcuts import render
from django.http import JsonResponse

from songs_list.models import Song, Artist


def index(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()
    context = {
        "songs": songs,
        "artists": artists
    }
    return render(request, 'songslist/index.html', context)


def get_all_songs(request):
    songs = Song.objects.all()
    content = []
    for song in songs:
        content.append({
            "id": song.id,
            "name": song.name,
        })

    return JsonResponse({"songs": content})
