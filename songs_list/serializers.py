from datetime import datetime

from songs_list.models import Song


class SongSerializer:

    @staticmethod
    def serializer(song_object):
        """
        Takes a Song object and returns a JSON dict
        """
        item = dict(
            id=song_object.id,
            name=song_object.name,
            album=song_object.album,
            year=song_object.release_year.year,
            youtube_link=song_object.youtube_link,
        )
        if song_object.song_artist:
            item["song_artist"] = dict(
                id=song_object.song_artist.id,
                first_name=song_object.song_artist.first_name,
                last_name=song_object.song_artist.last_name,
            )
        else:
            item["song_artist"] = None

        return item

    @staticmethod
    def deserializer(json_dict):
        """
        Takes a JSON dict and tries to return a SONG object
        """

        try:
            parsed_release_year = datetime(year=int(json_dict["release_year"]), month=1, day=1)
        except (KeyError, TypeError):
            parsed_release_year = None

        song = Song(
            name=json_dict["name"],
            album=json_dict["album"],
            release_year=parsed_release_year,
            youtube_link=json_dict["youtube_link"]
        )
        return song
