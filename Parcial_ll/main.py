# main.py
from productos import ControlPlagas, ControlFertilizantes, Antibiotico
from clientes import Cliente
from facturas import Factura


def mostrar_factura(cliente):
    factura = cliente.facturas[-1]  # Obtener la última factura generada
    print("\n\t--------------------------------------------------------")
    print("\t|                   FACTURA DE COMPRA                   |")
    print("\t--------------------------------------------------------")
    print(f"\tNombre del cliente: {cliente.nombre}")
    print(f"\tCédula del cliente: {cliente.cedula}")
    print(f"\tFecha de la factura: {factura.fecha}")
    print("\t--------------------------------------------------------")
    print("\t|    Producto    |    Precio Unitario    |    Cantidad    |    Total    |")
    print("\t--------------------------------------------------------")
    for producto in factura.productos:
        total_producto = producto.valor * producto.cantidad
        print(f"\t|{producto.nombre:<16}|{producto.valor:>23,.2f}|{producto.cantidad:>16}|{total_producto:>13,.2f}|")
    print("\t--------------------------------------------------------")
    print(f"\tTotal a pagar: {factura.calcular_total():,.2f}")
    print("\t--------------------------------------------------------")
    print("\n\tGracias por comprar aquí. Ha finalizado la compra.")
def main():
    print("\n\n\t ________________________________________________________")
    print("\t|                   TIENDA DEL CAMPO                     |")
    print("\t|  Productos agrícolas, Pesticidas, fertilizantes y más  |")
    print("\t|________________________________________________________|")

    while True:
        # Crear un cliente para cada compra
        nombre_cliente = input("\n\n\tIngrese el nombre del cliente: ")
        cedula_cliente = input("\tIngrese la cédula del cliente: ")
        cliente = Cliente(nombre_cliente, cedula_cliente)

        productos_factura = []

        while True:
            print("\n\tSeleccione un tipo de producto:")
            print("\t1. Control de Plagas")
            print("\t2. Control de Fertilizantes")
            print("\t3. Antibiótico")
            print("\t4. Finalizar compra")

            opcion = input("\tIngrese el número de opción: ")

            if opcion == "1":
                ica = input("\n\tIngrese el registro ICA: ")
                nombre = input("\tIngrese el nombre del producto: ")
                frecuencia_aplicacion = input("\tIngrese la frecuencia de aplicación (En días): ")
                valor = float(input("\tIngrese el valor del producto: "))
                periodo_carencia = input("\tIngrese el periodo de carencia en días: ")
                cantidad = int(input("\tIngrese la cantidad a comprar: "))  # Solicitar cantidad
                producto = ControlPlagas(ica, nombre, frecuencia_aplicacion, valor, periodo_carencia, cantidad)
                productos_factura.append(producto)
            elif opcion == "2":
                ica = input("\n\tIngrese el registro ICA: ")
                nombre = input("\tIngrese el nombre del producto: ")
                frecuencia_aplicacion = input("\tIngrese la frecuencia de aplicación (En días): ")
                valor = float(input("\tIngrese el valor del producto: "))
                ultima_aplicacion = input("\tIngrese la fecha de la última aplicación (DD-MM-AA): ")
                cantidad = int(input("\tIngrese la cantidad a comprar: "))  # Solicitar cantidad
                producto = ControlFertilizantes(ica, nombre, frecuencia_aplicacion, valor, ultima_aplicacion, cantidad)
                productos_factura.append(producto)
            elif opcion == "3":
                tipo_animal = input("\n\tIngrese el tipo de animal (Bovinos, Caprinos o Porcinos): ")
                nombre = input("\tIngrese el nombre del antibiótico: ")
                dosis = input("\tIngrese la dosis (entre 400Kg y 600Kg): ")
                valor = float(input("\tIngrese el valor del antibiótico: "))
                cantidad = int(input("\tIngrese la cantidad a comprar: "))  # Solicitar cantidad
                producto = Antibiotico(nombre, dosis, tipo_animal, valor, cantidad)
                productos_factura.append(producto)
            elif opcion == "4":
                if productos_factura:
                    fecha_factura = input("\n\tIngrese la fecha de la factura (DD-MM-AAAA): ")
                    factura = Factura(fecha_factura, productos_factura)
                    cliente.facturas.append(factura)
                    mostrar_factura(cliente)
                    break
                else:
                    print("\nNo se han seleccionado productos.")
            else:
                print("\nOpción no válida. Por favor, elija una opción válida.")

        decision = input("\n\t¿Desea realizar una nueva factura? (si/no): ")
        if decision.lower() != "si":
            print("\n\tHa finalizado la sesión.")
            break

if __name__ == "__main__":
    main()
