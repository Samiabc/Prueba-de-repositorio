package ec.edu.espe.booksalesystem.controller;

import ec.edu.espe.booksalesystem.model.Book;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Arelis Samantha Bonilla Cruz, Student, @ESPE
 */
public class BookController {
    public List<Book> getAllBooks() {
        List<Book> books = new ArrayList<>();

        books.add(new Book("Bajo la misma estrella", "John Green", 15.99));
        books.add(new Book("Las ventajas de ser invisible", "Stephen Chbosky", 14.50));
        books.add(new Book("Con amor, Simon", "Becky Albertalli", 13.99));
        books.add(new Book("A cinco pies de ti", "Rachael Lippincott", 16.00));
        books.add(new Book("Heartstopper Vol. 1", "Alice Oseman", 12.99));
        books.add(new Book("It Ends with Us", "Colleen Hoover", 17.99));
        books.add(new Book("A Curse So Dark and Lonely", "Brigid Kemmerer", 18.00));
        books.add(new Book("The Hate U Give", "Angie Thomas", 16.99));
        books.add(new Book("Once Upon a Broken Heart", "Stephanie Garber", 12.00));

        return books;
    }

    public Book getBookByTitle(String title) {
        for (Book book : getAllBooks()) {
            if (book.getTitle().equals(title)) {
                return book;
            }
        }
        return null;
    }
}