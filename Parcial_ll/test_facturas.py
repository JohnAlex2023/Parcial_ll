# test_facturas.py
import unittest
from facturas import Factura
from productos import ControlPlagas, ControlFertilizantes, Antibiotico

class TestFacturas(unittest.TestCase):
    def test_factura(self):
        productos_factura = [
            ControlPlagas("123ABC", "Plaguicida X", "7 días", 10.0, "15 días", 3),
            ControlFertilizantes("456DEF", "Fertilizante Y", "14 días", 20.0, "01-01-22", 5),
            Antibiotico("Antibiótico Z", "500 mg", "Bovinos", 15.0, 2)
        ]
        factura = Factura("01-01-2023", productos_factura)
        
        self.assertEqual(factura.fecha, "01-01-2023")
        self.assertEqual(len(factura.productos), 3)
        self.assertAlmostEqual(factura.calcular_total(), 160.0, places=2)  # Verificar el total con una tolerancia de 2 decimales

if __name__ == '__main__':
    unittest.main()
