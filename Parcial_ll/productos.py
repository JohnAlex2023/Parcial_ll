
# productos.py
class ProductoControl:
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor, cantidad):
        self.ica = ica
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor
        self.cantidad = cantidad

class ControlPlagas(ProductoControl):
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor, periodo_carencia, cantidad):
        super().__init__(ica, nombre, frecuencia_aplicacion, valor, cantidad)
        self.periodo_carencia = periodo_carencia

class ControlFertilizantes(ProductoControl):
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor, ultima_aplicacion, cantidad):
        super().__init__(ica, nombre, frecuencia_aplicacion, valor, cantidad)
        self.ultima_aplicacion = ultima_aplicacion

class Antibiotico(ProductoControl):
    def __init__(self, nombre, dosis, tipo_animal, valor, cantidad):
        super().__init__(None, nombre, None, valor, cantidad)
        self.dosis = dosis
        self.tipo_animal = tipo_animal
