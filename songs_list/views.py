import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from songs_list.models import Song
from songs_list.serializers import SongSerializer


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
            serialized_songs.append(SongSerializer.serializer(song))

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

        song = SongSerializer.deserializer(client_data)
        song.save()

        response_dict = dict(
            data=SongSerializer.serializer(song)
        )
        return JsonResponse(response_dict, status=201)


@csrf_exempt
def song(request, id):
    # GET /songs/1/ --> Find one object
    # DELETE /songs/1/ --> Deletes the selected object
    # UPDATE /songs/1/ --> Updates the selected object

    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return JsonResponse({"data": "object not found"}, status=404)

    method = request.method

    if method == "GET":
        response_dict = dict(
            data=SongSerializer.serializer(song)
        )
        return JsonResponse(response_dict, status=200)

    elif method == "DELETE":
        before_delete_id = song.id
        song.delete()
        return JsonResponse({"data": f"Deleted song #{before_delete_id}"}, status=204)
