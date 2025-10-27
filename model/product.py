

class Product:

    def __init__(self, id, name, new_price, quantity, total_price):
        self.id = id
        self.name = name
        self.new_price = new_price
        self.quantity = quantity
        self.total_price = total_price

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.name, self.new_price, self.quantity, self.total_price)