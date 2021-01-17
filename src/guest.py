class Guest:
    def __init__(self, name, cash, fav_song):
        self.name = name
        self.cash = cash
        self.fav_song = fav_song

    # EXTENSION
    
    def entry_fee(self, cash):
        for cash in range(self.cash):
            if self.cash >= 10:
                return True
            else:
                return False

    def playback(self, fav_song):
        for song in self.fav_song:
            if self.fav_song == "Genie in a Bottle":
                return "Woohoo!"
            else:
                return "Awww"

    # FURTHER EXTENSIONS
    
    def pay_entry_fee(self, cash):
        return self.cash - 10