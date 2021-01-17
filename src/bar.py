# FURTHER EXTENSIONS

class Bar:
    def __init__(self, name, cash, entry_fee):
        self.name = name
        self.cash = cash
        self.entry_fee = entry_fee
        self.list_of_drinks = [
            {"name": "Lemonade", "price": 3},
            {"name": "Coke", "price": 3},
            {"name": "Wine", "price": 5},
            {"name": "Pint", "price": 4}
        ]


    def find_drink_by_name(self, drink):
        found_drink = None
        for drink in self.list_of_drinks:
            if drink["name"] == name:
                found_drink = drink

        return found_drink

    def add_money_to_bar(self, cash):
        return self.cash + 10