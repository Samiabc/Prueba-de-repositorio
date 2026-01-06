from pymongo.collection import Collection
from model.sale import Sale
from utils.mongodb_connection import MongoDBConnection


class SaleController:
    def __init__(self):
        self.collection: Collection = (
            MongoDBConnection
            .get_database()
            .get_collection("Sales")
        )

    def save_sale(self, sale: Sale):
        document = {
            "product": sale.get_product(),
            "price": sale.get_price(),
            "quantity": sale.get_quantity(),
            "subtotal": sale.get_subtotal(),
            "iva": sale.get_iva(),
            "total": sale.get_total(),
            "date": sale.get_date()
        }

        self.collection.insert_one(document)

    def get_all_sales(self):
        sales = []

        for doc in self.collection.find():
            sale = Sale()
            sale.set_product(doc.get("product"))
            sale.set_price(doc.get("price"))
            sale.set_quantity(doc.get("quantity"))

            sales.append(sale)

        return sales