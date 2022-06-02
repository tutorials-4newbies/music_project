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
