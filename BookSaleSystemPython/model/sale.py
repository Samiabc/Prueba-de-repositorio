from datetime import datetime

class Sale:
    def __init__(self, book_title, unit_price, quantity):
        self.book_title = book_title
        self.unit_price = unit_price
        self.quantity = quantity
        self.total = unit_price * quantity
        self.date = datetime.now()