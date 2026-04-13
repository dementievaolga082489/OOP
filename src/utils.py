import json
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
JSON_FILE = DATA_DIR / "products.json"


def read_json(file_path: Path) -> list[dict[str, Any]]:
    """Функция читает JSON файл"""

    with open(file_path, "r", encoding="UTF-8") as file:
        data: list[dict[str, Any]] = json.load(file)

    return data


def create_objects_from_json(data: list[dict[str, Any]]) -> list[Category]:
    """Функция создает объекты классов"""

    categorys = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
            category["products"] = products
            categorys.append(Category(**category))
    return categorys


raw_data: list[dict[str, Any]] = read_json(JSON_FILE)
categorys_data: list[Category] = create_objects_from_json(raw_data)
print(raw_data)
print(categorys_data[0].name)
print(categorys_data[0].products)
