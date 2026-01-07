import tkinter as tk
from tkinter import font

class FrmMenu:

    def __init__(self, parent=None):
        self.window = tk.Toplevel(parent) if parent else tk.Tk()
        self.window.title("Menu")
        self.window.geometry("450x200")
        self.window.configure(bg="#896A46")

        lbl = tk.Label(
            self.window,
            text="WELCOME TO BOOK SALE SYSTEM",
            fg="white",
            bg="#896A46",
            font=("Perpetua", 16, "bold")
        )
        lbl.pack(pady=60)

        menubar = tk.Menu(self.window)
        report_menu = tk.Menu(menubar, tearoff=0)
        report_menu.add_command(label="Sales Report", command=self.open_sales_report)
        menubar.add_cascade(label="Report", menu=report_menu)

        sale_menu = tk.Menu(menubar, tearoff=0)
        sale_menu.add_command(label="Book Sale", command=self.open_book_sale)
        menubar.add_cascade(label="Sale", menu=sale_menu)

        self.window.config(menu=menubar)

    def open_book_sale(self):
        from view.frm_book_sale import FrmBookSale
        FrmBookSale(self.window)

    def open_sales_report(self):
        from view.frm_sales_report import FrmSalesReport
        FrmSalesReport(self.window)

    def run(self):
        self.window.mainloop()