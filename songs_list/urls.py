from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.get_all_songs, name='get_all_songs'),
    path('songs/<int:song_id>/', views.get_song, name='get_song')
]