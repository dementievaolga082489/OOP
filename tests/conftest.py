import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_2():
    return Product("Iphone 15", "128GB, Черный цвет, 48MP камера", 55000.0, 3)


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Автоматически сбрасывает счетчики категорий перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def category_first():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "128GB, Черный цвет, 48MP камера", 55000.0, 3),
            Product("Xiaomi Redmi Note 11", "128GB, Белый цвет, 50MP камера", 15500.0, 1),
        ],
    )


@pytest.fixture
def category_second():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def product_json():
    return [
        {
            "name": "Смартфоны",
            "description": (
                "Смартфоны, как средство не только коммуникации,"
                " но и получение дополнительных функций для удобства жизни"
            ),
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": (
                "Современный телевизор, который позволяет наслаждаться просмотром," " станет вашим другом и помощником"
            ),
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def category_iterator(category_first):
    return CategoryIterator(category_first)


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def smartphone_1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def category_without_product():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", []
    )
