class Book:
    def __init__(self, title="", author="", price=0.0):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return self.title