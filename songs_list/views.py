from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, response

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
        if song.release_year is not None:
            year = song.release_year.strftime("%Y")
        else:
            year = None
        content.append({
            "id": song.id,
            "name": song.name,
            "album": song.album,
            "release_year": year,
            "youtube_link": song.youtube_link
        })

    return JsonResponse({"songs": content})


def get_song(request, song_id):
    try:
        song = get_object_or_404(Song, id=song_id)
        if song.release_year is not None:
            year = song.release_year.strftime("%Y")
        else:
            year = None
        content = {
            "id": song.id,
            "name": song.name,
            "album": song.album,
            "release_year": year,
            "youtube_link": song.youtube_link
        }
        return JsonResponse({"song": content})
    except response.Http404:
        return JsonResponse({
            'error': 'The resource was not found'
        }, status=404)
