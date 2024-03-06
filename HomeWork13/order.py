from HomeWork13.factories.dish_factories import DishFactories

class OrderPart:
    #завдання 3
    @staticmethod
    def get_factory(dishes):
        if dishes == 'dish':
            return DishFactories()

order_part = OrderPart.get_factory('dish')
dish_factories_parts = order_part.cook_food('risotto')
print(dish_factories_parts)