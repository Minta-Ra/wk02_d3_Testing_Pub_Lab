import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Purple Rain", 7.99, 10)

    def test_drink_name(self):
        self.assertEqual("Purple Rain", self.drink.name)