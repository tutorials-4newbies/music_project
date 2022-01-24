from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.get_all_songs, name='get_all_songs')
]