class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.customer_drink = []

    def add_customer_drink(self, drink):
        self.customer_drink.append(drink)

    def deduct_from_wallet(self, amount):
        self.wallet -= amount