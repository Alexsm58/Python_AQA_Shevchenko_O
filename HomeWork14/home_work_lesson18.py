from HomeWork12.home_work_lesson15 import Train, TrainCar, TrainCar2


def test_vagon_len(first_vagon):
    vagon = TrainCar('Ivonna', '160', 66)

    first_vagon[vagon.passenger_name] = vagon
    assert len(first_vagon) == 1

def test_vagon1_len():
    pass

def test_vagons_multiply_fixture(first_vagon, vagon, vagon1):
    first_vagon[vagon.passenger_name] = vagon
    first_vagon[vagon1.passenger_name] = vagon1
    assert len(first_vagon) == 2

