from django.shortcuts import render

from songs_list.models import Song


def index(request):
    songs = Song.objects.all()
    context = {"songs": songs}
    return render(request, 'songslist/index.html', context)
