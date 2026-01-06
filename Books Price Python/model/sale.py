from datetime import datetime

class Sale:
    def __init__(self, product=None, price=0.0, quantity=0,
                 subtotal=0.0, iva=0.0, total=0.0, date=None):

        self.product = product
        self.price = price
        self.quantity = quantity
        self.subtotal = subtotal
        self.iva = iva
        self.total = total
        self.date = date

        if product is not None and price > 0 and quantity > 0:
            self.calculate_totals()
            self.date = datetime.now()

    def calculate_totals(self):
        self.subtotal = self.price * self.quantity
        self.iva = self.subtotal * 0.15
        self.total = self.subtotal + self.iva

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_subtotal(self):
        return self.subtotal

    def set_subtotal(self, subtotal):
        self.subtotal = subtotal

    def get_iva(self):
        return self.iva

    def set_iva(self, iva):
        self.iva = iva

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = total

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date