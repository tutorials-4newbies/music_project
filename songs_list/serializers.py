from datetime import datetime

from songs_list.models import Song


class SongValidationError(Exception):
    pass


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

        missing_parameters = []

        if "name" not in json_dict:
            missing_parameters.append("name")

        if "album" not in json_dict:
            missing_parameters.append("album")

        if "youtube_link" not in json_dict:
            missing_parameters.append("youtube_link")

        if "release_year" not in json_dict:
            missing_parameters.append("release_year")

        if len(missing_parameters) > 0:
            raise SongValidationError(f"missing parameters {missing_parameters}")
        else:
            song = Song(
                name=json_dict["name"],
                album=json_dict["album"],
                release_year=parsed_release_year,
                youtube_link=json_dict["youtube_link"]
            )
            return song
