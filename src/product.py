class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое отображение класса"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """Сложение стоимости всех товаров на складе."""
        total_cost_products = self.__price * self.quantity + other.__price * other.quantity
        return total_cost_products

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """
        Класс-метод для создания нового продукта из словаря.

        Args:
            product_dict: Словарь с ключами 'name', 'description', 'price', 'quantity'

        Returns:
            Product: Созданный объект продукта
        """
        product = cls(**product_dict)
        return product

    @property
    def price(self) -> float:
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для установки цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = value
