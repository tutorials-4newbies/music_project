from django.test import TestCase, Client
from songs_list.models import Song
from datetime import datetime


class SongTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_initial_state_returns_empty(self):
        response = self.client.get("/songs_list/songs/")
        self.assertEqual(response.status_code, 200)

        json_response = response.json()
        data = json_response["data"]

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)

    def test_single_song_response(self):
        # Add a song direct to the Database
        song = Song(
            name="test",
            album="album",
            release_year=datetime.now(),
            youtube_link="link"
        )
        song.save()

        # get list of all songs with one song
        response = self.client.get("/songs_list/songs/")
        self.assertEqual(response.status_code, 200)

        json_response = response.json()
        data = json_response["data"]

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

        our_song = data[0]
        self.assertEqual(our_song["name"], "test")
        self.assertEqual(our_song["album"], "album")
        self.assertEqual(our_song["year"], datetime.now().year)

    def test_add_a_new_song(self):
        song_to_send = {
            "name": "test",
            "album": "album",
            "release_year": 3000,
            "youtube_link": ""
        }

        post_response = self.client.post("/songs_list/songs/", data=song_to_send, content_type='application/json')
        self.assertEqual(post_response.status_code, 201)

        # get list of all songs with one song
        response = self.client.get("/songs_list/songs/")
        self.assertEqual(response.status_code, 200)

        json_response = response.json()
        data = json_response["data"]

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

        our_song = data[0]
        self.assertEqual(our_song["name"], "test")
        self.assertEqual(our_song["album"], "album")
        self.assertEqual(our_song["year"], 3000)

    def test_delete_a_song(self):
        # TODO: write it
        pass

    def test_replace_a_whole_song_object(self):
        song_to_send = {
            "name": "test_1",
            "album": "album_1",
            "release_year": 3000,
            "youtube_link": ""
        }

        post_response = self.client.post("/songs_list/songs/",
                         data=song_to_send,
                         content_type='application/json')

        json_response = post_response.json()
        first_song = json_response["data"]
        song_id = first_song["id"]

        # make a http call with new data to replace the song object
        new_song_to_send = {
            "name": "new_name",
            "album": "new_album",
            "release_year": 5000,
            "youtube_link": ""
        }
        replace_response = self.client.put(f"/songs_list/songs/{song_id}/",
                                           data=new_song_to_send,
                                           content_type='application/json')

        self.assertEqual(replace_response.status_code, 201)
        json_replace_response = replace_response.json()
        second_song = json_replace_response["data"]

        self.assertEqual(first_song["id"], second_song["id"])
        self.assertEqual(second_song["name"], "new_name")
        self.assertEqual(second_song["album"], "new_album")

    def test_cannot_replace_object_when_missing_fields_name_album_year(self):
        song_to_send = {
            "name": "test_1",
            "album": "album_1",
            "release_year": 3000,
            "youtube_link": ""
        }

        post_response = self.client.post("/songs_list/songs/",
                                         data=song_to_send,
                                         content_type='application/json')

        json_response = post_response.json()
        first_song = json_response["data"]
        song_id = first_song["id"]

        new_song_to_send = {
            "youtube_link": ""
        }
        replace_response = self.client.put(f"/songs_list/songs/{song_id}/",
                                           data=new_song_to_send,
                                           content_type='application/json')

        json_replace_response = replace_response.json()

        self.assertEqual(replace_response.status_code, 400)
        self.assertIn("error_message", json_replace_response)
        self.assertIn("missing parameters", json_replace_response["error_message"])
