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
            album=song.album
        )
        serialized_songs.append(item)

    response_dict = dict(
        data=serialized_songs
    )

    # send the list to the client app
    return JsonResponse(response_dict)


def song(request, id):
    # GET /songs/1/ --> One object
    song = Song.objects.get(pk=id)

    return JsonResponse(dict(
        song=dict(
            id=song.id,
            name=song.name
        )
    ))





    # POST /songs/ --> Create new object
    # UPDATE /songs/1/
    # DELETE /songs/1/
    pass
