from abc import ABC, abstractmethod

class Museum(ABC):
    def __init__(self, creation_year, assessed_value):
        self.creation_year = creation_year
        self.assessed_value = assessed_value

    @abstractmethod
    def museum_hall(self):
        pass

    def work_time(self):
        print('Work time from 10:00 AM to 8:00 PM')

class PaintingsArt(Museum):
    def __init__(self, creation_year, assessed_value):
        super().__init__(creation_year, assessed_value)
        self.price = price
        self.room = room
    def work_time(self):
        print('We don`t work on weekends')

    def paintings(self):
class FigurinesArt(Museum):
    def __init__(self, creation_year, assessed_value):
        super().__init__(creation_year, assessed_value)

    def work_time(self):
        print('We don`t work on saturday')
    def figurines(self):

class VesselsArt(Museum):
    def __init__(self, creation_year, assessed_value):
        super().__init__(creation_year, assessed_value)

    def work_time(self):
        print('We don`t work on sunday')
    def vessels(self):

