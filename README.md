# Reto-03
En el código se implementa un sistema de facturación para un restaurante utilizando los conceptos de herencia y composición. Se modela un menú con distintos tipos de ítems (bebidas, platos fuertes, postres, etc.) y se calcula la cuenta total de un cliente, aplicando descuentos e impuestos cuando corresponda.
Se adjuntó el código en Python y su respectiva representación UML.

## Características Generales 

- Se tiene la Clase base `MenuItem` con atributos y comportamiento común para todos los ítems.
- Subclases especializadas para distintos tipos de alimentos y bebidas.
- La Clase `Order` registra pedidos, aplica descuentos, calcula impuestos y genera la factura.

## Ejemplo de uso: 
bebida = Beverage("Refresco", 2.50, "medium")
plato = MainCourse("Pasta", 12.00, "regular", "pollo", "espagueti")

PEDIDO:
pedido = Order("Juan Pérez")
pedido.add_item(bebida, 2)  
pedido.add_item(plato)   

pedido.bill()

