import pytest

from src.category import Category
from src.product import Product


def test_category_init(category_first, category_second):

    assert category_first.name == "Смартфоны"
    assert (
        category_first.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_first.products_list) == 3

    assert Category.category_count == 2
    assert category_first.category_count == 2
    assert category_second.category_count == 2

    assert category_first.product_count == 4
    assert category_second.product_count == 4


def test_products_property(category_first):
    """Тест геттера на вывод списка продуктов в виде строк"""
    assert category_first.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 55000.0 руб. Остаток: 3 шт.\n"
        "Xiaomi Redmi Note 11, 15500.0 руб. Остаток: 1 шт.\n"
    )


def test_add_product_success():
    """Тест успешного добавления товара в категорию"""
    # Создаем тестовые продукты
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 5)
    product2 = Product("Мышь", "Беспроводная мышь", 1000, 10)

    # Создаем категорию с одним товаром
    category = Category("Электроника", "Различная электроника", [product1])

    # Сохраняем начальное количество продуктов в категории
    initial_product_count = Category.product_count

    # Добавляем новый продукт
    category.add_product(product2)

    # Проверяем, что продукт добавился в список
    assert len(category.products_list) == 2
    assert category.products_list[-1] == product2

    assert Category.product_count == initial_product_count + 1


def test_category_str(category_first):
    assert str(category_first) == "Смартфоны, количество продуктов: 9 шт."


def test_category_iterator(category_iterator):
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator).name == "Iphone 15"
    assert next(category_iterator).name == "Xiaomi Redmi Note 11"


def test_add_product_error(product, category_first):
    with pytest.raises(TypeError):
        category_first.add_product(1)


def test_add_product(product_2, smartphone_1):
    product_2.products = smartphone_1

def test_middle_price(category_first, category_without_product):
    assert category_first.middle_price() == 83500
    assert category_without_product.middle_price() == 0