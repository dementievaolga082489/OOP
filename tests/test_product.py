from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product():
    """Тест на успешное создание нового продукта"""

    product_dict = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

    product = Product.new_product(product_dict)
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 180000.0
    product.quantity = 5


def test_product_update(capsys, product):
    """Тестирование установки новой цены"""
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = 100
    assert product.price == 100
