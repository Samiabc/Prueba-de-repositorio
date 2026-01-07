package ec.edu.espe.booksalesystem.model;

import java.util.Date;

/**
 *
 * @author Arelis Samantha Bonilla Cruz, Student, @ESPE
 */
public class Sale {

    private String bookTitle;
    private double unitPrice;
    private int quantity;
    private double subtotal;
    private double total;
    private Date date;

    public Sale(String bookTitle, double unitPrice, int quantity) {
        this.bookTitle = bookTitle;
        this.unitPrice = unitPrice;
        this.quantity = quantity;
        calculateTotals();
        this.date = new Date();
    }

    private void calculateTotals() {
        setSubtotal(getUnitPrice() * getQuantity());
        setTotal(getSubtotal());
    }

    public double getSubtotal() {
        return subtotal;
    }

    public double getTotal() {
        return total;
    }

    public String getBookTitle() {
        return bookTitle;
    }

    public void setBookTitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }

    public double getUnitPrice() {
        return unitPrice;
    }

    public void setUnitPrice(double unitPrice) {
        this.unitPrice = unitPrice;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public void setSubtotal(double subtotal) {
        this.subtotal = subtotal;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    } 
}