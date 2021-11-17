import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drink

# Inherit from unittest
class TestPub(unittest.TestCase):
    
    def setUp(self):
        # instance with new Pub object
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Beer", 3.00)
        self.customer = Customer("John Doe", 25.00)

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
        drink = Drink("Beer", 2.99)
        self.pub.add_drink_to_pub_stock(drink)
        self.assertEqual([drink], self.pub.drinks_stock)


    def test_sell_to_customer(self):
        self.pub.add_drink_to_pub_stock(self.drink)
        self.customer.add_customer_drink(self.pub.drinks_stock)
        self.pub.drinks_stock.clear()
        self.assertEqual(1, len(self.customer.customer_drink))
        self.assertEqual(0, len(self.pub.drinks_stock))

    def test_deduct_money_from_customer(self):
        self.pub.increase_till(self.drink.price)
        self.customer.deduct_from_wallet(self.drink.price)
        self.assertEqual(22.00, self.customer.wallet)
        self.assertEqual(103.00, self.pub.till)




    