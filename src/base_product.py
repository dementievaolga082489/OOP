from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, является родительским для класса продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
