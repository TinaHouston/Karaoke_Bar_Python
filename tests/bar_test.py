# FURTHER EXTENSIONS

import unittest

from src.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Bar Room 1", 1000, 10)


    def test_bar_has_name(self):
        self.assertEqual("Bar Room 1", self.bar.name)

    def test_bar_has_total_cash(self):
        self.assertEqual(1000, self.bar.cash)

    def test_bar_has_entry_fee(self):
        self.assertEqual(10, self.bar.entry_fee)

    def test_bar_has_4_drinks(self):
        self.assertEqual(4, len(self.bar.list_of_drinks))

    def test_find_drink_by_name(self):
        self.bar.found_drink = "Lemonade"
        self.assertEqual({"name": "Lemonade", "price": 3}, self.bar.list_of_drinks[0])

    def test_can_add_money_to_bar(self):
        self.assertEqual(1010, self.bar.add_money_to_bar(self.bar))



