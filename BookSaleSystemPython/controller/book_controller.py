from model.book import Book

class BookController:

    def get_all_books(self):
        return [
            Book("Bajo la misma estrella", "John Green", 15.99),
            Book("Las ventajas de ser invisible", "Stephen Chbosky", 14.50),
            Book("Con amor, Simon", "Becky Albertalli", 13.99),
            Book("A cinco pies de ti", "Rachael Lippincott", 16.00),
            Book("Heartstopper Vol. 1", "Alice Oseman", 12.99),
            Book("It Ends with Us", "Colleen Hoover", 17.99),
            Book("A Curse So Dark and Lonely", "Brigid Kemmerer", 18.00),
            Book("The Hate U Give", "Angie Thomas", 16.99),
            Book("Once Upon a Broken Heart", "Stephanie Garber", 12.00)
        ]

    def get_book_by_title(self, title):
        for book in self.get_all_books():
            if book.title == title:
                return book
        return None