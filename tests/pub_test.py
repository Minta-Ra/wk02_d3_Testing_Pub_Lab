import unittest
from src.pub import Pub

# Inherit from unittest
class TestPub(unittest.TestCase):
    
    def setUp(self):
        # instance with new Pub object
        self.pub = Pub("The Prancing Pony", 100.00)

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

    