class TrainCar:
    #we count the cars in the train, the people in the cars, the length of the car and the train
    def __init__(self, passenger_name, destination, place=None):
        self.passenger_name = passenger_name
        self.destination = destination
        self.place = place
        self.passengers = dict()    #create dictionary to store passengers in carriages
        self.class_train = 'First'

    def __add__(self, other):   #add wagon instances
        return Train(self.class_train, other.second_class_train)

    def __radd__(self, other):   #add reverse instance of cars
        return Train(self.class_train, other.second_class_train)

    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, name):
        self._passenger_name = name


class TrainCar2:
    #create the first carriage
    def __init__(self, passenger_name, destination, place=None):
        self.second_class_train = 'Second'
        self.passenger_name = passenger_name
        self.destination = destination
        self.place = place
        self.passengers = dict()    #create dictionary to store passengers in carriages

    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, name):
        self._passenger_name = name

        
class Train:
    #create the second carriage
    def __init__(self, class_train, second_class_train):
        self.class_train = class_train
        self.second_class_train = second_class_train
        self.stages = dict()    #create an empty dictionary for storing cars on a train

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

print(f'\tNumber of cars: {len(first_vagon)}')

#displaying passengers and their seats
print("\tRailway carriage: 1")
for passenger, car in first_vagon.stages.items():
    print(f"\tPassenger: {passenger},\n\tPlace: {car.place}")

#we display the number of passengers in the first carriage
print(f'\tNumber of passengers in the first carriage: {len(first_vagon)}')

#removal of passengers and their seats from the second carriage
print("\tRailway carriage: 2")
for passenger, car in train_car2.passengers.items():
    print(f"\tPassenger: {passenger},\n\tPlace: {car.place}")

#we display the number of passengers in the second carriage
print(f'\tNumber of passengers in the first carriage: {len(train_car2.passengers)}')