class Rooms:
    def __init__(self, name, capacity, songs):
        self.name = name
        self. capacity = capacity
        self.guests = []
        self.songs = songs
        self.bar = []


    # Function might be needed for PDA?
    def guest_count(self):
        return len(self.guests)

    def check_in(self, guest):
        self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)
   
   
#    Function needed for PDA
    def add_song(self, song):
        self.songs.append(song)

    def too_many_guests_return_too_full(self, guest):
            for guest in self.guests:
                if len(self.guests) > 10:
                    return "Too full, sorry"
                else: 
                    return "Come on in"


# FURTHER EXTENSIONS

    def add_bar(self, bar):
        self.bar.append(bar)
