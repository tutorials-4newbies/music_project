from http import HTTPStatus
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt

from songs_list.models import Song, Artist
from songs_list.serializers import song_obj_to_dict


def index(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()
    context = {
        "songs": songs,
        "artists": artists
    }
    return render(request, 'songslist/index.html', context)


@csrf_exempt
def songs_view(request):
    if request.method == "GET":
        songs = Song.objects.all()
        content = []
        for song in songs:
            content.append(song_obj_to_dict(song))
        return JsonResponse({"songs": content})

    if request.method == "POST":
        data = request.POST
        song = Song()
        song.name = data["name"]
        song.album = data["album"]
        song.save()
        content = song_obj_to_dict(song)
        return JsonResponse({"song": content}, status=HTTPStatus.CREATED)


def get_song(request, song_id):
    try:
        song = get_object_or_404(Song, id=song_id)
        content = song_obj_to_dict(song)
        return JsonResponse({"song": content})
    except response.Http404:
        return JsonResponse({
            'error': 'The resource was not found'
        }, status=HTTPStatus.NOT_FOUND)


def create_song(request):
    pass
