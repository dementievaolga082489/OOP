from src.category import Category


def test_category_init(category_first, category_second):

    assert category_first.name == "Смартфоны"
    assert (
        category_first.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_first.products) == 3

    assert Category.category_count == 2
    assert category_first.category_count == 2
    assert category_second.category_count == 2

    assert category_first.product_count == 4
    assert category_second.product_count == 4
