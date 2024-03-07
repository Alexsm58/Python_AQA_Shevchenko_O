import pytest
from HomeWork12.home_work_lesson15 import Train, TrainCar, TrainCar2

@pytest.fixture
def first_vagon():
    print('I`m cool first vagon')
    yield Train('lux', 'polulux')


@pytest.fixture
def vagon():
    yield TrainCar('Ivonna', '160', 66)

@pytest.fixture
def vagon1():
    yield TrainCar('Igor', '180', 99)

@pytest.fixture
def populated_vagon(first_vagon, vagon, vagon1):
    first_vagon[vagon.passenger_name] = vagon
    first_vagon[vagon1.passenger_name] = vagon1
    yield first_vagon
