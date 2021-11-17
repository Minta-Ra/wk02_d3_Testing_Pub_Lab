import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drink
from src.food import Food

# Inherit from unittest
class TestPub(unittest.TestCase):
    
    def setUp(self):
        # instance with new Pub object
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Beer", 3.00, 5)
        self.drink2 = Drink("Purple Rain", 8.00, 6)
        self.customer = Customer("John Doe", 25.00, 24)
        self.customer2 = Customer("Hurbert Bridges", 5.00, 17)
        self.chips = Food("Chips", 2.00, 4)
        self.salad = Food("Salad", 2.50, 1)

    # Test if pub has a name - property
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    # @unittest.skip("delete this line to run the test")
    # Test a method
    def test_increase_till(self):
        # 3 AAA:
        # Arrange - set up 
        # Act - if anything needs to be done
        self.pub.increase_till(2.50)
        # Assert - change property

        # expected = 102.50
        # actual = self.pub.till
        # self.assertEqual(expected, actual)
        # OR:
        self.assertEqual(102.5, self.pub.till)


    def test_add_drink_to_pub_stock(self):
        drink = Drink("Beer", 2.99, 3)
        self.pub.add_drink_to_pub_stock(drink)
        self.assertEqual([drink], self.pub.drinks_stock)

    def test_sell_to_customer(self):
        self.pub.sell_to_customer(self.customer, self.drink)
        self.assertEqual(22.00, self.customer.wallet)
        self.assertEqual(103.00, self.pub.till)

    def test_customer_age(self):
        self.assertEqual(True, self.pub.check_customer_age(self.customer))
        self.assertEqual(False, self.pub.check_customer_age(self.customer2))
        
    def test_check_drunkenness(self):
        drunk = self.customer.add_drunkenness(self.drink)
        self.assertEqual(True, self.pub.check_customer_drunkenness(drunk))
        
    def test_customer_bought_food(self):
        self.customer.drunkenness = 11
        self.pub.serve_food(self.customer, self.chips)
        self.assertEqual(7, self.customer.drunkenness)