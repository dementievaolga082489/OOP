
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

    def add_product(self, product: Product) -> None:
        """Метод добавления товаров в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер выводит список товаров в виде строк"""
        product_str = ""
        for product_ in self.__products:
            product_str += f"{product_.name}, {product_.price} руб. Остаток: {product_.quantity} шт.\n"
        return product_str

    @property
    def products_list(self) -> List[Product]:
        """Возвращает список продуктов"""
        return self.__products
