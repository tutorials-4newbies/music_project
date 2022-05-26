from http import HTTPStatus
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from songs_list.models import Song, Artist


# TODO:
#  1. Create a class to hold the serilaizer logic for converting data
#     from the database to the client and from the client to the databse
#  2. Create the DELETE endpoint


def index(request):
    songs = Song.objects.all()
    context = {
        "songs": songs,
    }
    return render(request, 'songs_list/index.html', context)


@csrf_exempt
def songs(request):
    # GET /songs/ --> All objects
    # POST /songs/ --> Create a new object

    # get a list of all songs in the database
    method = request.method

    if method == "GET":
        songs = Song.objects.all()

        serialized_songs = []
        for song in songs:
            item = dict(
                id=song.id,
                name=song.name,
                album=song.album,
                year=song.release_year.year,
                youtube_link=song.youtube_link,
            )
            if song.song_artist:
                item["song_artist"] = dict(
                    id=song.song_artist.id,
                    first_name=song.song_artist.first_name,
                    last_name=song.song_artist.last_name,
                )
            else:
                item["song_artist"] = None

            serialized_songs.append(item)

        response_dict = dict(
            data=serialized_songs
        )
        # send the list to the client app
        return JsonResponse(response_dict, status=200)

    elif method == "POST":
        client_data = json.loads(request.body)

        if "name" in client_data:
            name = client_data["name"]
        else:
            return JsonResponse({"data": "Missing the 'name' parameter"}, status=400)

        try:
            parsed_release_year = datetime(
                year=client_data["release_year"],
                month=1,
                day=1
            )
        except (KeyError, TypeError):
            parsed_release_year = None

        song = Song(
            name=name,
            album=client_data["album"],
            release_year=parsed_release_year,
            youtube_link=client_data["youtube_link"]
        )
        song.save()
        # TODO: Return the created object including ID
        response_object = {}
        return JsonResponse({"data": response_object}, status=201)


def song(request, id):
    # GET /songs/1/ --> Find one object
    # DELETE /songs/1/ --> Deletes the selected object
    # UPDATE /songs/1/ --> Updates the selected object
    # TODO: Add DELETE method

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
