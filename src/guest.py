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