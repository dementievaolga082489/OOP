
from src.product import Product


class LawnGrass(Product):
    """Дочерний класс 'Трава газонная' принимающий родительский класс Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass"| Product) -> float:
        """Сложение стоимости всех товаров 'газонная трава' на складе."""
        if type(other) is LawnGrass:
            total_cost_products = self.price * self.quantity + other.price * other.quantity
            return total_cost_products
        raise TypeError
