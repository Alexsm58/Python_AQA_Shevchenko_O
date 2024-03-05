from abc import ABC, abstractmethod

class Factory(ABC):
    _order_type = ''

    @abstractmethod
    def cook_food(self, name):
        pass