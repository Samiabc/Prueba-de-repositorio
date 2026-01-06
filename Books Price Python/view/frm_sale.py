import tkinter as tk
from tkinter import messagebox
from controller.sale_controller import SaleController
from model.sale import Sale


class FrmSale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Ventas")
        self.geometry("400x300")
        self.resizable(False, False)

        self.sale_controller = SaleController()

        self.create_widgets()

    def create_widgets(self):
        lbl_title = tk.Label(self, text="Sistema de Ventas", font=("Arial", 18))
        lbl_title.pack(pady=10)

        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="Producto:").grid(row=0, column=0, sticky="e")
        self.txt_product = tk.Entry(frame)
        self.txt_product.grid(row=0, column=1)

        tk.Label(frame, text="Precio:").grid(row=1, column=0, sticky="e")
        self.txt_price = tk.Entry(frame)
        self.txt_price.grid(row=1, column=1)

        tk.Label(frame, text="Cantidad:").grid(row=2, column=0, sticky="e")
        self.txt_quantity = tk.Entry(frame)
        self.txt_quantity.grid(row=2, column=1)

        btn_save = tk.Button(
            self,
            text="Calcular y Guardar",
            command=self.save_sale
        )
        btn_save.pack(pady=15)

    def validate_product(self):
        if not self.txt_product.get().strip():
            self.txt_product.config(highlightbackground="red", highlightthickness=1)
            return False
        self.txt_product.config(highlightthickness=0)
        return True

    def validate_price(self):
        try:
            price = float(self.txt_price.get())
            if price <= 0:
                raise ValueError
            self.txt_price.config(highlightthickness=0)
            return True
        except ValueError:
            self.txt_price.config(highlightbackground="red", highlightthickness=1)
            return False

    def validate_quantity(self):
        try:
            quantity = int(self.txt_quantity.get())
            if quantity <= 0:
                raise ValueError
            self.txt_quantity.config(highlightthickness=0)
            return True
        except ValueError:
            self.txt_quantity.config(highlightbackground="red", highlightthickness=1)
            return False

    def save_sale(self):
        if not (
            self.validate_product()
            and self.validate_price()
            and self.validate_quantity()
        ):
            messagebox.showerror(
                "Datos inválidos",
                "Corrige los campos en rojo antes de guardar"
            )
            return

        product = self.txt_product.get().strip()
        price = float(self.txt_price.get())
        quantity = int(self.txt_quantity.get())

        sale = Sale(product, price, quantity)
        self.sale_controller.save_sale(sale)

        self.show_summary(sale)

        messagebox.showinfo("Éxito", "Venta guardada correctamente")

        self.txt_product.delete(0, tk.END)
        self.txt_price.delete(0, tk.END)
        self.txt_quantity.delete(0, tk.END)

    def show_summary(self, sale: Sale):
        dialog = tk.Toplevel(self)
        dialog.title("Detalle de Pago")
        dialog.geometry("250x150")
        dialog.resizable(False, False)
        dialog.grab_set()

        tk.Label(dialog, text="Subtotal:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        tk.Label(dialog, text=f"$ {sale.get_subtotal():.2f}").grid(row=0, column=1)

        tk.Label(dialog, text="IVA (15%):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Label(dialog, text=f"$ {sale.get_iva():.2f}").grid(row=1, column=1)

        tk.Label(dialog, text="Total:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Label(dialog, text=f"$ {sale.get_total():.2f}").grid(row=2, column=1)


if __name__ == "__main__":
    app = FrmSale()
    app.mainloop()