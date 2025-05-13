# Reto-03
En el código se implementa un sistema de facturación para un restaurante utilizando los conceptos de herencia y composición. Se modela un menú con distintos tipos de ítems (bebidas, platos fuertes, postres, etc.) y se calcula la cuenta total de un cliente, aplicando descuentos e impuestos cuando corresponda.
 - Está el código en Python y su respectiva representación UML.

## Características Generales 

- Se tiene la Clase base `MenuItem` con atributos y comportamiento común para todos los ítems.
- Subclases especializadas para distintos tipos de alimentos y bebidas.
- La Clase `Order` registra pedidos, aplica descuentos, calcula impuestos y genera la factura.

## Clase `MenuItem`

La clase base `MenuItem` representa un ítem genérico del menú. Tiene los atributos:

- `name`: nombre del ítem.
- `base_price`: precio base.
- `size`: tamaño (small, medium, large).

Esta es la clase padre para todos los tipos específicos de ítems en el menú, lo que facilita su reutilización.

---

## Subclases de `MenuItem`

### `Beverage`
- **Atributo:** `contains_alcohol`  
  Indica si la bebida contiene alcohol.

---

### `Appetizer`
- **Atributos**
-  `with_sauce`: indica si la entrada lleva alguna salsa.
-  `with_lemon`: relata si la entrada viene con limón.

---

### `Soup`
- **Atributos:**
  - `temperature`: dice si la sopa está caliente.
  - `with_tostacos`: indica si posee una adición de tostacos.
  - `with_avocado`: muestra lleva aguacate.

---

### `MainCourse`
- **Atributos:**
  - `protein`: proteína del plato fuerte (pollo, carne, etc.).
  - `carbs`: carbohidrato acompañante (arroz, papas, etc.).
  - `is_vegetarian`: si es un plato vegetariano.
  - `walnut_allergy`, `cereal_allergy`, `egg_allergy`: si contiene algo que genere una alérgia.

--- 

### `Dessert`
- **Atributos:**
  - `lactose_intolerante`: opción sin lactosa.
  - `chocolate_addition`: adiciona chocolate-
  - `ice_cream_addition`: incluye helado.

---

### `SideDish`
- **Atributos:**
  - `is_spicy`: muestra si es picante.
  - `extra_cheese`: indica si tiene extra queso.

---  

### `Salad`
- **Atributo:** 
  - `dressing_type`: tipo de aderezo (César, vinagreta, etc.).
  - `chicken_addition`: Indica si se tiene una adición de pollo.

---

### `Coffee`
- **Atributos:**
  - `coffee_type`: estilo del café que se prepara.  
  - `milk_type`: es el tipo de leche.

---

### `KidsMeal`
- **Atributos:**
  - `main_item`: plato fuerte de los niños.
  - `side_item`: adición infantil.
  - `drink`: bebida infantil.
  - `toy`: opción de incluir un juguete.

---

### `Special`
- *Ofrece descuentos especiales*:
- - **Atributos:**
  - `day_of_week`: descuentos según el día de la semana.
  - `is_chef_recommendation`: si es una recomendación del chef.

---

## Clase `Order`

Gestiona el pedido. Gestiona los ítems seleccionados y calcular los montos correspondientes.

### Métodos principales:

- **`add_item(item, quantity=1)`**  
  Añade ítems al pedido con la cantidad indicada.

- **`calculate_subtotal()`**  
  Calcula el total de los productos antes de aplicar impuestos o descuentos.

- **`apply_discounts()`**  
  Aplica descuentos automáticos si se cumplen ciertas condiciones (Si se paga más de 50 o si se tienen más de cuatro productos).

- **`calculate_tax()`**  
  Calcula el impuesto aplicable al subtotal.

- **`calculate_total()`**  
  Devuelve el total final a pagar, considerando impuestos y descuentos.

- **`bill()`**  
  Imprime una factura detallada que incluye:
  - Nombre del cliente.
  - Ítems pedidos, cantidades y precios unitarios.
  - Subtotal.
  - Descuentos aplicados.
  - Impuestos.
  - Total final a pagar.

## Métodos usados en la nayoría de subclases: 
- **`get_price()`**: modifica el precio dependiendo del criterio dado.
- **`__str__()`**: devuelve una cadena que indica lo que lleva el producto.

## Herencia:
- `MenuItem` actúa como clase padre para todos los tipos de ítems del menú.
- Subclases como `Beverage`, `Soup`, `MainCourse`, etc., heredan de `MenuItem` y con el **super()** heredan el nombre, precio y el tamaño.

### Composición
- El objeto `Order` contiene múltiples objetos `MenuItem` (Se compone de esos objetos).
- Los ítems se agreganmediante el método `add_item()`.

  
## Ejemplo de uso
```python
# Crear instancias de ítems del menú
bebida = Beverage("Refresco", 2.50, "medium")
plato = MainCourse("Pasta", 12.00, "regular", "pollo", "espagueti")

# Crear pedido y agregar ítems
pedido = Order("Juan Pérez")
pedido.add_item(bebida, 2)  
pedido.add_item(plato)

# Generar factura
pedido.bill()
