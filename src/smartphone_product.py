from src.product import Product


class Smartphone(Product):
    """Дочерний класс 'Смартфон' принимающий родительский класс Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone" | Product) -> float:
        """Сложение стоимости всех товаров 'смартфонов' на складе."""
        if type(other) is Smartphone:
            total_cost_products = self.price * self.quantity + other.price * other.quantity
            return total_cost_products
        raise TypeError
