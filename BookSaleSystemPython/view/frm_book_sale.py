import tkinter as tk
from tkinter import ttk, messagebox
from controller.book_controller import BookController
from controller.sale_controller import SaleController
from model.sale import Sale

class FrmBookSale:

    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Book Sale")
        self.window.geometry("400x200")
        self.window.configure(bg="#FFFFFF")

        self.book_controller = BookController()
        self.sale_controller = SaleController()

        tk.Label(self.window, text="Book:", font=("Perpetua", 12)).grid(row=0, column=0, padx=10, pady=5)
        self.cmb_book = ttk.Combobox(self.window, state="readonly", font=("Perpetua", 12))
        self.cmb_book.grid(row=0, column=1)

        tk.Label(self.window, text="Unit Price:", font=("Perpetua", 12)).grid(row=1, column=0)
        self.txt_price = tk.Entry(self.window, state="readonly", font=("Perpetua", 12))
        self.txt_price.grid(row=1, column=1)

        tk.Label(self.window, text="Quantity:", font=("Perpetua", 12)).grid(row=2, column=0)
        self.spn_quantity = tk.Spinbox(self.window, from_=1, to=100, font=("Perpetua", 12))
        self.spn_quantity.grid(row=2, column=1)

        tk.Button(self.window, text="Save", font=("Perpetua", 12), command=self.save_sale).grid(row=3, column=1, pady=10)

        self.load_books()
        self.cmb_book.bind("<<ComboboxSelected>>", self.on_book_selected)

        menubar = tk.Menu(self.window)
        system_menu = tk.Menu(menubar, tearoff=0)
        system_menu.add_command(label="Back to Menu", command=self.back_to_menu)
        menubar.add_cascade(label="System", menu=system_menu)
        self.window.config(menu=menubar)

    def load_books(self):
        books = self.book_controller.get_all_books()
        self.cmb_book["values"] = [book.title for book in books]

    def on_book_selected(self, event):
        book = self.book_controller.get_book_by_title(self.cmb_book.get())
        if book:
            self.txt_price.config(state="normal")
            self.txt_price.delete(0, tk.END)
            self.txt_price.insert(0, str(book.price))
            self.txt_price.config(state="readonly")

    def save_sale(self):
        try:
            sale = Sale(
                self.cmb_book.get(),
                float(self.txt_price.get()),
                int(self.spn_quantity.get())
            )
            self.sale_controller.save_sale(sale)
            messagebox.showinfo("Success", f"Sale saved!\nTotal: ${sale.total:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def back_to_menu(self):
        self.window.destroy()
        from view.frm_menu import FrmMenu
        FrmMenu(self.window.master)