class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till 
        self.drinks_stock = []

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_pub_stock(self, drink):
        self.drinks_stock.append(drink)

