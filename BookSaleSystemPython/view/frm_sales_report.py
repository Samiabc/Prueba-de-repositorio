import tkinter as tk
from tkinter import ttk
from controller.sale_controller import SaleController

class FrmSalesReport:

    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Sales Report")
        self.window.geometry("600x300")
        self.window.configure(bg="#FFFFFF")

        self.sale_controller = SaleController()

        columns = ("Book", "Unit Price", "Quantity", "Total", "Date")
        self.table = ttk.Treeview(self.window, columns=columns, show="headings", height=10)
        for col in columns:
            self.table.heading(col, text=col)
        self.table.pack(fill=tk.BOTH, expand=True)

        tk.Button(self.window, text="Reload", font=("Perpetua", 12), command=self.load_sales).pack(pady=5)
        self.load_sales()

        menubar = tk.Menu(self.window)
        system_menu = tk.Menu(menubar, tearoff=0)
        system_menu.add_command(label="Back to Menu", command=self.back_to_menu)
        menubar.add_cascade(label="System", menu=system_menu)
        self.window.config(menu=menubar)

    def load_sales(self):
        for row in self.table.get_children():
            self.table.delete(row)
        for sale in self.sale_controller.get_all_sales():
            self.table.insert("", tk.END, values=(
                sale.book_title,
                sale.unit_price,
                sale.quantity,
                sale.total,
                sale.date.strftime("%Y-%m-%d %H:%M")
            ))

    def back_to_menu(self):
        self.window.destroy()
        from view.frm_menu import FrmMenu
        FrmMenu(self.window.master)