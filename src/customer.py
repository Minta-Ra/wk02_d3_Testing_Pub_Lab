class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.customer_drink = []
        self.age = age
        self.drunkenness = 0

    def add_customer_drink(self, drink):
        self.customer_drink.append(drink)

    def deduct_from_wallet(self, amount):
        self.wallet -= amount
        
    def add_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
        return self.drunkenness
    
    def deduct_drunkenness(self, food):
        self.drunkenness -= food.rejuv_level
        return self.drunkenness