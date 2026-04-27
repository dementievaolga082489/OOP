import pytest


def test_lawngrass_init(lawn_grass_1):
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.description == "Элитная трава для газона"
    assert lawn_grass_1.price == 500.0
    assert lawn_grass_1.quantity == 20
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"
    assert lawn_grass_1.color == "Зеленый"


def test_lawngrass_add(lawn_grass_1, lawn_grass_2):
    assert lawn_grass_1 + lawn_grass_2 == 16750


def test_lawngrass_add_error(lawn_grass_1):
    with pytest.raises(TypeError):
        lawn_grass_1 + 1
