import unittest

from src.rooms import Rooms
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.song_1 = Song("Suddenly I see", "KT Tunstall")
        self.song_2 = Song("What Makes you Beautiful", "One Direction")

        songs = [self.song_1, self.song_2]

        self.room = Rooms("Karaoke Room 1", 10, songs)
        self.guest = Guest("Harriet", 100, "One Love")
       

    def test_room_has_name(self):
        self.assertEqual("Karaoke Room 1", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)


    def test_room_starts_with_no_guests(self):
        self.assertEqual(0, self.room.guest_count())

    def test_check_in_guest(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, self.room.guest_count())

    def test_check_out_guest(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(0, self.room.guest_count())

    
    # Two functions below here needed for PDA -- REMINDER
    def test_number_of_songs_in_room(self):
        self.assertEqual(2, len(self.room.songs))
    
    def test_add_song_to_room(self):
        self.room.add_song(self.song_1)
        self.assertEqual(3, len(self.room.songs))

    #  End of PDA requirement

    # EXTENSION

    def test_more_guests_than_capacity(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.assertEqual("Too full, sorry", self.room.too_many_guests_return_too_full(self.guest))

    def test_room_has_enough_capacity_for_guests(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.assertEqual("Come on in", self.room.too_many_guests_return_too_full(self.guest))

