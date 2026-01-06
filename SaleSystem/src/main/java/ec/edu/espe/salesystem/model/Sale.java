package ec.edu.espe.salesystem.model;

import java.util.Date;

/**
 *
 * @author Arelis Samantha Bonilla Cruz, Student, @ESPE
 */
public class Sale {
    private String product;
    private double price;
    private int quantity;
    private double subtotal;
    private double iva;
    private double total;
    private Date date;

    public Sale(String product, double price, int quantity, double subtotal, double iva, double total, Date date) {
        this.product = product;
        this.price = price;
        this.quantity = quantity;
        this.subtotal = subtotal;
        this.iva = iva;
        this.total = total;
        this.date = date;
    }
    
    public Sale() {
    }
    
    public Sale(String product, double price, int quantity) {
        this.product = product;
        this.price = price;
        this.quantity = quantity;
        calculateTotals();
        this.date = new Date();
    }
    
    private void calculateTotals() {
        subtotal = price * quantity;
        iva = subtotal * 0.15;
        total = subtotal + iva;
    }

    /**
     * @return the product
     */
    public String getProduct() {
        return product;
    }

    /**
     * @param product the product to set
     */
    public void setProduct(String product) {
        this.product = product;
    }

    /**
     * @return the price
     */
    public double getPrice() {
        return price;
    }

    /**
     * @param price the price to set
     */
    public void setPrice(double price) {
        this.price = price;
    }

    /**
     * @return the quantity
     */
    public int getQuantity() {
        return quantity;
    }

    /**
     * @param quantity the quantity to set
     */
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    /**
     * @return the subtotal
     */
    public double getSubtotal() {
        return subtotal;
    }

    /**
     * @param subtotal the subtotal to set
     */
    public void setSubtotal(double subtotal) {
        this.subtotal = subtotal;
    }

    /**
     * @return the iva
     */
    public double getIva() {
        return iva;
    }

    /**
     * @param iva the iva to set
     */
    public void setIva(double iva) {
        this.iva = iva;
    }

    /**
     * @return the total
     */
    public double getTotal() {
        return total;
    }

    /**
     * @param total the total to set
     */
    public void setTotal(double total) {
        this.total = total;
    }

    /**
     * @return the date
     */
    public Date getDate() {
        return date;
    }

    /**
     * @param date the date to set
     */
    public void setDate(Date date) {
        this.date = date;
    }
    
}
