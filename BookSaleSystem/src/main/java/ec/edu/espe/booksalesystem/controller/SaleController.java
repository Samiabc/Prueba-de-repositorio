package ec.edu.espe.booksalesystem.controller;

import com.mongodb.client.MongoCollection;
import ec.edu.espe.booksalesystem.model.Sale;
import ec.edu.espe.booksalesystem.utils.MongoDBConnection;
import java.util.ArrayList;
import java.util.List;
import org.bson.Document;

/**
 *
 * @author Arelis Samantha Bonilla Cruz, Student, @ESPE
 */
public class SaleController {
    private MongoCollection<Document> collection;

    public SaleController() {
        collection = MongoDBConnection
                .getDatabase()
                .getCollection("BookSales");
    }

    public void saveSale(Sale sale) {
        Document doc = new Document("bookTitle", sale.getBookTitle())
                .append("unitPrice", sale.getUnitPrice())
                .append("quantity", sale.getQuantity())
                .append("subtotal", sale.getSubtotal())
                .append("total", sale.getTotal())
                .append("date", sale.getDate());

        collection.insertOne(doc);
    }

    public List<Sale> getAllSales() {
        List<Sale> sales = new ArrayList<>();

        for (Document doc : collection.find()) {
            Sale sale = new Sale(
                    doc.getString("bookTitle"),
                    doc.getDouble("unitPrice"),
                    doc.getInteger("quantity")
            );
            sales.add(sale);
        }
        return sales;
    }
}