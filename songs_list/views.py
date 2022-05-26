from http import HTTPStatus

from django.shortcuts import render
from django.http import JsonResponse

from songs_list.models import Song, Artist


def index(request):
    songs = Song.objects.all()
    context = {
        "songs": songs,
    }
    return render(request, 'songs_list/index.html', context)


def songs(request):
    # GET /songs/ --> All objects
    # get a list of all songs in the database
    songs = Song.objects.all()

    serialized_songs = []
    for song in songs:
        item = dict(
            id=song.id,
            name=song.name,
            album=song.album,
            year=song.release_year.year,
            youtube_link=song.youtube_link,
            song_artist=dict(
                id=song.song_artist.id,
                first_name=song.song_artist.first_name,
                last_name=song.song_artist.last_name,
            )
        )
        serialized_songs.append(item)

    response_dict = dict(
        data=serialized_songs
    )

    # send the list to the client app
    return JsonResponse(response_dict)


def song(request, id):
    # GET /songs/1/ --> One object
    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return JsonResponse({"data": "object not found"}, status=404)

    return JsonResponse(dict(
        data=dict(
            id=song.id,
            name=song.name,
            album=song.album,
            year=song.release_year.year,
            youtube_link=song.youtube_link,
            song_artist=dict(
                id=song.song_artist.id,
                first_name=song.song_artist.first_name,
                last_name=song.song_artist.last_name,
            )
        )
    ))



    # POST /songs/ --> Create new object
    # UPDATE /songs/1/
    # DELETE /songs/1/
    pass
