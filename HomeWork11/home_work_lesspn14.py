from abc import ABC, abstractmethod

class Museum(ABC):    #add abstract class
    #5th direction of ООР for art museum objects
    def __init__(self, creation_year, assessed_value, room, status=201):
        self.creation_year = creation_year
        self.assessed_value = assessed_value
        self.room = room
        self.__status = status
    @abstractmethod    #add abstractmethod
    def museum_hall(self):
        pass

    def _work_time(self):
        print('Work time from 10:00 AM to 8:00 PM')

    @property    #add property
    def status(self):
        return self.__status

    @status.setter    #add setter
    def status(self, options):
        self.__status = options



class PaintingsArt(Museum):    #inheritance
    def __init__(self, creation_year, assessed_value, room):
        super().__init__(creation_year, assessed_value, room)

    def museum_hall(self, hours):
        print(f'hours of work {hours} place in room{self.room}')

    def __ticket_price(self, price=10):    #hiding inside a class
        print(f'Ticket price in paintings room {price}$')

    def _work_time(self):    #hiding usage in classes, modules or packages
        print('We don`t work on weekends')
        self.__ticket_price()

    def encapsulation_pac(self):
        self.museum_hall()
        self.__ticket_price()
        self._work_time()
        self._work_time()


class FigurinesArt(Museum):
    def __init__(self, creation_year, assessed_value, room):
        super().__init__(creation_year, assessed_value, room)

    def museum_hall(self, hours):
        print(f'hours of work {hours} place in room{self.room}')
    def _work_time(self):
        print('We don`t work on saturday')


class VesselsArt(Museum):
    def __init__(self, creation_year, assessed_value, room):
        super().__init__(creation_year, assessed_value, room)

    def museum_hall(self, hours):
        print(f'hours of work {hours} place in room {self.room}')
    def _work_time(self):
        print('We don`t work on sunday')


paintings = PaintingsArt(325, 70000, 'yellow')
paintings.museum_hall(10)
paintings._work_time()

print(paintings.status)
paintings.status = 301
print(paintings.status)

figurines = FigurinesArt(519, 150000, 'braun')
figurines.museum_hall(12)
figurines._work_time()

print(figurines.status)
figurines.status = 404
print(figurines.status)

vessels = VesselsArt(705, 5000, 'green')
vessels.museum_hall(8)
vessels._work_time()

print(vessels.status)
vessels.status = 500
print(vessels.status)