class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till 
        self.drinks_stock = []
        self.age_check = 18
        self.drunk_refusal = 10

    def increase_till(self, amount):
        self.till += amount

    def add_drink_to_pub_stock(self, drink):
        self.drinks_stock.append(drink)

    def check_customer_age(self, age):
        if age.age >= self.age_check:
            return True
        else:
            return False
        
    def check_customer_drunkenness(self, drunk):
        while drunk < self.drunk_refusal:
            return True