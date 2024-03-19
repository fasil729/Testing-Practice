class Product:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")
        if not isinstance(price, (int, float)) or not isinstance(quantity, int):
            raise TypeError("Price must be a number and quantity must be an integer")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotal(self):
        return self.price * self.quantity

