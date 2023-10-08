# test_productos.py
import unittest
from productos import ControlPlagas, ControlFertilizantes, Antibiotico

class TestProductos(unittest.TestCase):
    def test_control_plagas(self):
        producto = ControlPlagas("123ABC", "Plaguicida X", "7 días", 10.0, "15 días", 3)
        self.assertEqual(producto.ica, "123ABC")
        self.assertEqual(producto.nombre, "Plaguicida X")
        self.assertEqual(producto.frecuencia_aplicacion, "7 días")
        self.assertEqual(producto.valor, 10.0)
        self.assertEqual(producto.periodo_carencia, "15 días")
        self.assertEqual(producto.cantidad, 3)

    def test_control_fertilizantes(self):
        producto = ControlFertilizantes("456DEF", "Fertilizante Y", "14 días", 20.0, "01-01-22", 5)
        self.assertEqual(producto.ica, "456DEF")
        self.assertEqual(producto.nombre, "Fertilizante Y")
        self.assertEqual(producto.frecuencia_aplicacion, "14 días")
        self.assertEqual(producto.valor, 20.0)
        self.assertEqual(producto.ultima_aplicacion, "01-01-22")
        self.assertEqual(producto.cantidad, 5)

    def test_antibiotico(self):
        producto = Antibiotico("Antibiótico Z", "500 mg", "Bovinos", 15.0, 2)
        self.assertEqual(producto.nombre, "Antibiótico Z")
        self.assertEqual(producto.dosis, "20ml POR CADA 100KG DE PESO")
        self.assertEqual(producto.tipo_animal, "Bovinos")
        self.assertEqual(producto.valor, 15.0)
        self.assertEqual(producto.cantidad, 2)

if __name__ == '__main__':
    unittest.main()
