package ec.edu.espe.booksalesystem.utils;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;

/**
 *
 * @author Arelis Samantha Bonilla Cruz, Student, @ESPE
 */
public class MongoDBConnection {
    private static MongoDatabase database;

    private MongoDBConnection() {
    }

    public static MongoDatabase getDatabase() {
        if (database == null) {
            MongoClient client = MongoClients.create("mongodb+srv://Arelis:Arelis2006@cluster0.qdn4zsf.mongodb.net/");
            database = client.getDatabase("BookSalesDB");
        }
        return database;
    }
}