
# facturas.py
class Factura:
    def __init__(self, fecha, productos):
        self.fecha = fecha
        self.productos = productos

    def calcular_total(self):
        return sum(producto.valor * producto.cantidad for producto in self.productos)
