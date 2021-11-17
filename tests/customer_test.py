import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jane Smith", 50.00, 23)

    def test_customer_has_wallet(self):
        self.assertEqual(50.00, self.customer.wallet)

   