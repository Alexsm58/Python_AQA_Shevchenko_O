class TrainCar:
    def __init__(self, passenger_name, destination, place=None):
        self.passenger_name = passenger_name
        self.destination = destination
        self.place = place
        self.passengers = dict()  # Создаем пустой словарь для хранения вагонов
        self.class_train = 'First'

    def __add__(self, other):
        return Train(self.class_train, other.second_class_train)

    def __radd__(self, other):
        return Train(self.class_train, other.second_class_train)

    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, name):
        self._passenger_name = name


class TrainCar2:
    def __init__(self, passenger_name, destination, place=None):
        self.second_class_train = 'Second'
        self.passenger_name = passenger_name
        self.destination = destination
        self.place = place
        self.passengers = dict()  # Создаем пустой словарь для хранения пассажиров

    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, name):
        self._passenger_name = name

class Train:
    def __init__(self, class_train, second_class_train):
        self.class_train = class_train
        self.second_class_train = second_class_train
        self.stages = dict()

    def __setitem__(self, key, value):
        self.stages[key] = value

    def __len__(self):
        return len(self.stages)

    def __str__(self):
        return f'{self.__class__.__name__}: \n\tclass_train = {self.class_train}\n\tsecond_class_train = {self.second_class_train}'


train_car = TrainCar(None, None, None)
train_car2 = TrainCar2(None, None, None)  # Передаем параметры при создании объекта TrainCar2
train = train_car + train_car2
print(train)

first_vagon = Train('lux', 'polulux')

vagon = TrainCar('Ivonna', '160', 66)
vagon1 = TrainCar('Igor', '180', 99)
first_vagon[vagon.passenger_name] = vagon
first_vagon[vagon1.passenger_name] = vagon1

vagon2 = TrainCar2('Ivon', '260', 88)
train_car2.passengers[vagon2.passenger_name] = vagon2

print(f'\tКоличество вагонов: {len(first_vagon)}')

# Вывод пассажиров и их мест
print("\tВагон: 1")
for passenger, car in first_vagon.stages.items():
    print(f"\tПассажир: {passenger},\n\tМесто: {car.place}")

# Выводим количество пассажиров в первом вагоне
print(f'\tКоличество пассажиров в первом вагоне: {len(first_vagon)}')

# Вывод пассажиров и их мест второго вагона
print("\tВагон: 2")
for passenger, car in train_car2.passengers.items():
    print(f"\tПассажир: {passenger},\n\tМесто: {car.place}")

# Выводим количество пассажиров во втором вагоне
print(f'\tКоличество пассажиров во втором вагоне: {len(train_car2.passengers)}')