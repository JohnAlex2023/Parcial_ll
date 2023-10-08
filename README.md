# Parcial_ll
Herencia_Asociaciones_Python
Requerimientos Funcionales

Usted ha sido contratado para realizar un sistema de facturación para una tienda agrí-
cola. Donde cada factura (o Pedido) está compuesto de los productos que serán comprados.

Esta tienda solamente maneja Productos de Control (Fertilizantes y Controles de plagas)
y medicina para animales de granja, precisamente antibióticos.
Los Productos de Control tendrán como características un registro ICA, el nombre del
producto y la frecuencia de aplicación (es decir, cada cuanto periodo se aplica el producto.
Cada 15 días, cada 30 días, etc) así como también el valor del producto. Tenga en cuenta
que el Control de Plagas y el Control de Fertilizantes son un tipo de Productos de Control,
donde el primero tiene como característica un periodo de carencia (es el tiempo legalmente
establecido, expresado usualmente en número de días que debe transcurrir entre la última
aplicación de un fitosanitario y la cosecha) y el segundo la fecha de la última aplicación de
este Producto.

Por otro lado, en la tienda se venden antibióticos para bovinos y porcinos donde las ca-
racterísticas de este producto son: nombre del producto, dosis (entre 400Kg y 600Kg), tipo

de animal al que se le puede aplicar (Bovinos, caprinos o porcinos) y precio.
Tenga en cuenta que al ser una tienda agrícola los Clientes (con atributos nombre y
cédula) son habituales por lo tanto el mismo cliente puede tener dentro de su historial de

1

compras, muchas Pedidos (o Facturas) asociadas. Una Factura como tal debe tener fecha en
que se realizó la factura y el valor total de la compra.

Tenga en cuenta que todos los atributos de las clases son obligatorios. Con esta infor-
mación puede diseñar los casos de prueba.

2. Requerimientos de la Arquitectura de Software
Esta aplicación debe de ser construida bajo los siguientes parámetros arquitectónicos:
1. Los componentes para separar responsabilidades (Modelo, Test).
2. Utilicen el concepto de Módulos y NameSpace.
3. Cada Clase debe de estar en un archivo separado dentro del Componente de Modelo.
