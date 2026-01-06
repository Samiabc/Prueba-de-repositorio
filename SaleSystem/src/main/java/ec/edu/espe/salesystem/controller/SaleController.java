package ec.edu.espe.salesystem.controller;

import com.mongodb.client.MongoCollection;
import ec.edu.espe.salesystem.model.Sale;
import ec.edu.espe.salesystem.utils.MongoDBConnection;
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
                .getCollection("Sales");
    }

    public void saveSale(Sale sale) {
        Document document = new Document("product", sale.getProduct())
                .append("price", sale.getPrice())
                .append("quantity", sale.getQuantity())
                .append("subtotal", sale.getSubtotal())
                .append("iva", sale.getIva())
                .append("total", sale.getTotal())
                .append("date", sale.getDate());

        collection.insertOne(document);
    }

    public List<Sale> getAllSales() {
        List<Sale> sales = new ArrayList<>();

        for (Document doc : collection.find()) {
            Sale sale = new Sale();
            sale.setProduct(doc.getString("product"));
            sale.setPrice(doc.getDouble("price"));
            sale.setQuantity(doc.getInteger("quantity"));

            sales.add(sale);
        }
        return sales;
    }
}
