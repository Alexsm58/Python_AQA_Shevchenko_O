import csv

class CSVFileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    # Чтение файла
    def read_file(self):
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                print(row)


csv_manager = CSVFileManager('new.csv')
csv_manager.read_file()