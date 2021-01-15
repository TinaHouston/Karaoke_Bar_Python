import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Landslide", "Fleetwood Mac")

    
    def test_song_has_name(self):
        self.assertEqual("Landslide", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Fleetwood Mac", self.song.artist)
        