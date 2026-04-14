import json
from unittest.mock import mock_open, patch

from src.utils import JSON_FILE, read_json


def test_read_json(product_json) -> None:  # Фикстура как аргумент
    """Тест на успешное открытие json файла"""
    with patch("builtins.open", mock_open(read_data=json.dumps(product_json))):
        result = read_json(JSON_FILE)
        assert result == product_json
