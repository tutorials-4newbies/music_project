from http import HTTPStatus
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from songs_list.models import Song, Artist
from songs_list.serializers import song_obj_to_dict
import json


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

        name = data.get("name")
        if not name:
            return JsonResponse({'error': 'Missing parameter: name'}, status=HTTPStatus.BAD_REQUEST)
        else:
            song.name = name

        album = data.get("album")
        if not album:
            return JsonResponse({'error': 'Missing parameter: album'}, status=HTTPStatus.BAD_REQUEST)
        else:
            song.album = album

        release_year = data.get("release_year")
        if release_year:
            try:
                song.release_year = datetime.strptime(release_year, "%Y")
            except ValueError:
                return JsonResponse(
                    {'error': 'Bad format: release_year. needs to be a year, example "2002"'},
                    status=HTTPStatus.BAD_REQUEST
                )

        youtube_link = data.get("youtube_link")
        if youtube_link:
            song.youtube_link = youtube_link

        song.save()
        content = song_obj_to_dict(song)
        return JsonResponse({"song": content}, status=HTTPStatus.CREATED)


@csrf_exempt
def single_song_view(request, song_id):
    try:
        song = get_object_or_404(Song, id=song_id)
    except response.Http404:
        return JsonResponse({'error': 'The resource was not found'}, status=HTTPStatus.NOT_FOUND)

    if request.method == "GET":
        content = song_obj_to_dict(song)
        return JsonResponse({"song": content})

    if request.method == "DELETE":
        song.delete()
        return JsonResponse({'Success': 'The song was deleted'}, status=HTTPStatus.OK)

    if request.method == "PATCH":
        data = json.loads(request.body.decode('utf-8'))
        name = data.get("name")
        if name:
            song.name = name

        album = data.get("album")
        if album:
            song.album = album

        release_year = data.get("release_year")
        if release_year:
            try:
                song.release_year = datetime.strptime(str(release_year), "%Y")
            except ValueError:
                return JsonResponse(
                    {'error': 'Bad format: release_year. needs to be a year, example "2002"'},
                    status=HTTPStatus.BAD_REQUEST
                )

        youtube_link = data.get("youtube_link")
        if youtube_link:
            song.youtube_link = youtube_link

        song.save()
        content = song_obj_to_dict(song)
        return JsonResponse({"song": content}, status=HTTPStatus.OK)
