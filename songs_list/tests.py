from django.test import TestCase, Client


class SongTestCase(TestCase):

    def test_no_songs_in_db(self):
        # http://127.0.0.1:8000/songs_list/songs/
        client = Client()
        response = client.get("/songs_list/songs/")
        self.assertEqual(response.status_code, 404)
