from utils.mongodb_connection import MongoDBConnection
from model.sale import Sale

class SaleController:

    def __init__(self):
        self.collection = MongoDBConnection().get_collection("BookSales")

    def save_sale(self, sale: Sale):
        self.collection.insert_one({
            "bookTitle": sale.book_title,
            "unitPrice": sale.unit_price,
            "quantity": sale.quantity,
            "total": sale.total,
            "date": sale.date
        })

    def get_all_sales(self):
        sales = []
        for doc in self.collection.find():
            sale = Sale(
                doc["bookTitle"],
                doc["unitPrice"],
                doc["quantity"]
            )
            sale.date = doc["date"]
            sales.append(sale)
        return sales