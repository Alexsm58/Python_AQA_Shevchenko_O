import pytest
from HomeWork12.home_work_lesson15 import Train, TrainCar, TrainCar2

@pytest.mark.regression
@pytest.mark.smoke
def test_vagon_len(first_vagon):
    vagon = TrainCar('Ivonna', '160', 66)

    first_vagon[vagon.passenger_name] = vagon
    assert len(first_vagon) == 1

@pytest.mark.regression
def test_vagons_multiply_fixture(first_vagon, vagon, vagon1):
    first_vagon[vagon.passenger_name] = vagon
    first_vagon[vagon1.passenger_name] = vagon1
    assert len(first_vagon) == 2

@pytest.mark.regression
def test_vagons_complex_fixture(populated_vagon):
    assert len(populated_vagon) == 2

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize(
    'train_class, train_passenger_name',
    [('a', 'a'), ('c', 'c')]
)
def test_first_vagon_parametrised(first_vagon, train_class, train_passenger_name):

    train_instance = Train(train_class, train_passenger_name)    #создаем экземпляр класса Train
    first_vagon[train_passenger_name] = train_instance    #присваиваем его в словарь first_vagon
    assert train_instance.class_train == train_class    #проверяем, что значение объекта train_instance.class_train соответствует переданному train_class

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize(
    'train, train_class, train_passenger_name',
    [(Train('a', 'b'), 'a', 'b'),
     (Train('c', 'd'), 'c', 'd')],
    ids=['first case', 'second case']
)
def test_vagon_parametrised(first_vagon, train, train_class, train_passenger_name):
    train_instance = train
    first_vagon[train_passenger_name] = train_instance
    assert train_instance.class_train == train_class

@pytest.mark.smoke
@pytest.mark.skip(reason='test for check the pass')
def test_vagon1_len():
    pass