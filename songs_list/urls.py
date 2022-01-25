from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.songs_view, name='songs_view'),
    path('songs/<int:song_id>/', views.get_song, name='get_song')
]