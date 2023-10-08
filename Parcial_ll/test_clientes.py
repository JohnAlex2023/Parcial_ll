# test_clientes.py
import unittest
from clientes import Cliente

class TestClientes(unittest.TestCase):
    def test_cliente(self):
        cliente = Cliente("John Alex", "1234567890")
        self.assertEqual(cliente.nombre, "John Alex")
        self.assertEqual(cliente.cedula, "1234567890")
        self.assertEqual(len(cliente.facturas), 0)

if __name__ == '__main__':
    unittest.main()
