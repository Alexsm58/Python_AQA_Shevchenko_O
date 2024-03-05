from HomeWork13.factories import Factory, Pasta, Pizza, Risotto

class DishFactories(Factory):
    _order_type = 'dish'
    def __init__(self):
        self.name = 'Michelin'
        self._positions = ['Risotto', 'Pasta', 'Pizza']


    @property
    def positions(self):
        return self._positions


    def cook_food(self, name):
        if name == 'risotto':
            return Risotto()
        elif name == 'pasta':
            return Pasta()
        elif name == 'pizza':
            return Pizza()

