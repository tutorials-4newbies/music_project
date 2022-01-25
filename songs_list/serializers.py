def song_obj_to_dict(song_obj):

    if song_obj.release_year is not None:
        year = song_obj.release_year.strftime("%Y")
    else:
        year = None

    song_dict = {
        "id": song_obj.id,
        "name": song_obj.name,
        "album": song_obj.album,
        "release_year": year,
        "youtube_link": song_obj.youtube_link
    }

    return song_dict
