class MenuItem:
    def __init__(self, name: str, price: float, size: str = "regular") -> None:
        self.name: str = name
        self.price: float = price
        self.size: str = size

    def total_price(self, quantity: int = 1) -> float:
        return self.price * quantity

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str, is_alcohol: bool = False) -> None:
        super().__init__(name, price, size)
        self.is_alcohol: bool = is_alcohol

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.8
        elif self.size == "large":
            self.price *= 1.4

    def __str__(self) -> str:
        alcohol: str = ""
        if self.is_alcohol:
            alcohol = "alcoholic"
        return (
            f"{self.name}{alcohol} {self.size.capitalize()} "
            f"- (${self.price:.2f})"
        )


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, with_sauce: bool = False, with_lemon: bool = False) -> None:
        super().__init__(name, price)
        self.with_sauce: bool = with_sauce
        self.with_lemon: bool = with_lemon

    def __str__(self) -> str:
        sauce: str = ""
        lemon: str = ""
        if self.with_sauce:
            sauce = "with homemade sauce"
        if self.with_lemon:
            lemon = "and lemon"
        return f"{self.name}{sauce}{lemon} - (${self.price:.2f})"


class Soup(MenuItem):
    def __init__(self, name: str, price: float, size: str, temperature: str = "regular",
                 with_tostacos: bool = False, with_avocado: bool = False) -> None:
        super().__init__(name, price, size)
        self.temperature: str = temperature
        self.with_tostacos: bool = with_tostacos
        self.with_avocado: bool = with_avocado

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.9
        elif self.size == "large":
            self.price *= 1.2
        if self.with_tostacos:
            self.price *= 1.05
        if self.with_avocado:
            self.price *= 1.1

    def __str__(self) -> str:
        avocado: str = ""
        tostacos: str = ""
        if self.with_avocado:
            avocado = "avocado addition"
        if self.with_tostacos:
            tostacos = "tostacos addition"
        return (
            f"{self.name}{self.temperature}{avocado}{tostacos} "
            f" {self.size.capitalize()} "
            f"- (${self.price:.2f})"
        )


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, size: str, protein: str, carbs: str,
                 is_vegetarian: bool = False, walnut_allergy: bool = False, cereal_allergy: bool = False,
                 egg_allergy: bool = False) -> None:
        super().__init__(name, price, size)
        self.protein: str = protein
        self.carbs: str = carbs
        self.is_vegetarian: bool = is_vegetarian
        self.walnut_allergy: bool = walnut_allergy
        self.cereal_allergy: bool = cereal_allergy
        self.egg_allergy: bool = egg_allergy

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.9
        elif self.size == "large":
            self.price *= 1.3
        if self.is_vegetarian:
            self.price *= 2
        if self.walnut_allergy or self.cereal_allergy or self.egg_allergy:
            self.price *= 1.05

    def __str__(self) -> str:
        vegetarian: str = ""
        if self.is_vegetarian:
            vegetarian = "vegetarian"
        return (
            f"{self.name}{self.protein}{self.carbs}{vegetarian} "
            f" {self.size.capitalize()} "
            f"- (${self.price:.2f})"
        )


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, lactose_intolerant: bool = False,
                 chocolate_addition: bool = False, ice_cream_addition: bool = False) -> None:
        super().__init__(name, price)
        self.lactose_intolerant: bool = lactose_intolerant
        self.chocolate_addition: bool = chocolate_addition
        self.ice_cream_addition: bool = ice_cream_addition

    def calculate_price(self) -> None:
        if self.lactose_intolerant:
            self.price *= 1.4
        if self.chocolate_addition:
            self.price *= 1.1
        if self.ice_cream_addition:
            self.price *= 1.2

    def __str__(self) -> str:
        return f"{self.name} - (${self.price:.2f})"


class SideDish(MenuItem):
    def __init__(self, name: str, price: float, size: str, is_spicy: bool = False, extra_cheese: bool = False) -> None:
        super().__init__(name, price, size)
        self.is_spicy: bool = is_spicy
        self.extra_cheese: bool = extra_cheese

    def calculate_price(self) -> None:  
        if self.size == "small":
            self.price *= 0.7
        elif self.size == "large":
            self.price *= 1.3
        if self.is_spicy:
            self.price *= 1.1
        if self.extra_cheese:
            self.price *= 1.15

    def __str__(self) -> str:
        spicy: str = ""
        cheese: str = ""
        if self.is_spicy:
            spicy = " (spicy)"
        if self.extra_cheese:
            cheese = " (extra cheese)"
        return f"{self.name}{spicy}{cheese} {self.size} - ${self.price:.2f}"


class Salad(MenuItem):
    def __init__(self, name: str, price: float, size: str, dressing_type: str = "house",
                 chicken_addition: bool = False) -> None:
        super().__init__(name, price, size)
        self.dressing_type: str = dressing_type
        self.chicken_addition: bool = chicken_addition

    def calculate_price(self) -> None:
        if self.size == "large":
            self.price *= 1.4
        if self.chicken_addition:
            self.price *= 1.1

    def __str__(self) -> str:
        chicken: str = ""
        if self.chicken_addition:
            chicken = "chicken"
        return (
            f"{self.size} {self.name} with {self.dressing_type} "
            f" dressing - {chicken} ${self.price:.2f}"
        )


class Coffee(MenuItem):
    def __init__(self, name: str, price: float, size: str, coffee_type: str = "espresso",
                 milk_type: str | None = None) -> None:
        super().__init__(name, price, size)
        self.coffee_type: str = coffee_type
        self.milk_type: str | None = milk_type

    def calculate_price(self) -> None:
        if self.size == "small":
            self.price *= 0.8
        elif self.size == "large":
            self.price *= 1.5
        if self.milk_type in ["almond", "soy"]:
            self.price *= 1.2

    def __str__(self) -> str:
        milk: str = f" with {self.milk_type} milk" if self.milk_type else ""
        return f"{self.size} {self.coffee_type}{milk} - ${self.price:.2f}"


class KidsMeal(MenuItem):
    def __init__(self, name: str, price: float, main_item: str, side_item: str, drink: str, toy: bool = True) -> None:
        super().__init__(name, price)
        self.main_item: str = main_item
        self.side_item: str = side_item
        self.drink: str = drink
        self.toy: bool = toy

    def calculate_price(self) -> None:
        if not self.toy:
            self.price *= 0.9

    def __str__(self) -> str:
        toy: str = " with toy" if self.toy else ""
        return (
            f"Kids Meal: {self.main_item} + {self.side_item} + "
            f" {self.drink}{toy} - ${self.price:.2f}"
        )


class Special(MenuItem):
    def __init__(self, name: str, price: float, day_of_week: str, is_chef_recommendation: bool = False) -> None:
        super().__init__(name, price)
        self.day_of_week: str = day_of_week
        self.is_chef_recommendation: bool = is_chef_recommendation

    def calculate_price(self) -> None:
        if self.day_of_week in ["Tuesday", "Wednesday"]:
            self.price *= 0.85
        if self.is_chef_recommendation:
            self.price *= 1.1

    def __str__(self) -> str:
        chef: str = " (Chef's Recommendation)" if self.is_chef_recommendation else ""
        return (
            f"Special of the day ({self.day_of_week}): {self.name}{chef} - "
            f" ${self.price:.2f}"
        )


class Order:
    def __init__(self, customer_name: str) -> None:
        self.customer_name: str = customer_name
        self.items: list[MenuItem] = []
        self.discount: float = 0
        self.tax_rate: float = 0.08

    def add_item(self, menu_item: MenuItem, quantity: int = 1) -> None:
        for _ in range(quantity):
            menu_item.calculate_price()
            self.items.append(menu_item)

    def calculate_subtotal(self) -> float:
        return sum(item.price for item in self.items)

    def apply_discounts(self) -> None:
        self.discount = 0
        subtotal: float = self.calculate_subtotal()
        if subtotal >= 50:
            self.discount += subtotal * 0.05
        if len(self.items) >= 4:
            self.discount += subtotal * 0.02

    def calculate_tax(self) -> float:
        return (self.calculate_subtotal() - self.discount) * self.tax_rate

    def calculate_total(self) -> float:
        self.apply_discounts()
        subtotal: float = self.calculate_subtotal()
        tax: float = self.calculate_tax()
        return (subtotal - self.discount) + tax

    def bill(self) -> None:
        print("BILL:")
        print(f"{self.customer_name}")
        print("Items:")
        for item in self.items:
            print(item)
        subtotal: float = self.calculate_subtotal()
        tax: float = self.calculate_tax()
        total: float = self.calculate_total()
        print(f"Subtotal: ${subtotal:.2f}")
        if self.discount > 0:
            print(f"Discount ${self.discount:.2f}")
        print(f"Taxes: ({self.tax_rate*100:.0f}%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")



"""EJEMPLO:
bebida = Beverage("Refresco", 2.50, "medium")
plato = MainCourse("Pasta", 12.00, "regular", "pollo", "espagueti")

PEDIDO:
pedido = Order("Juan Romero")
pedido.add_item(bebida, 2)  
pedido.add_item(plato)      

# Generar factura
pedido.bill()

"""
