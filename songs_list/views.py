from django.shortcuts import render
from django.http import JsonResponse

from songs_list.models import Song, Artist


def index(request):
    songs = Song.objects.all()
    context = {
        "songs": songs,
    }
    return render(request, 'songs_list/index.html', context)
