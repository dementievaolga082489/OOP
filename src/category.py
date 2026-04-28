from typing import List

from src.product import Product


class Category:
    """Класс для представления категории продукта"""

    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Строковое отображение класса"""
        # Подсчет общего количества продуктов в категории продукта
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product: Product) -> None:
        """Метод добавления товаров в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Геттер выводит список товаров в виде строк"""
        product_str = ""
        for product_ in self.__products:
            product_str += f"{str(product_)}\n"
        return product_str

    @property
    def products_list(self) -> List[Product]:
        """Возвращает список продуктов"""
        return self.__products

    def middle_price(self):
        """Подсчитывает средний ценник всех товаров."""
        try:
            return sum([product.price for product in self.__products] ) / len(self.__products)
        except ZeroDivisionError:
            return 0