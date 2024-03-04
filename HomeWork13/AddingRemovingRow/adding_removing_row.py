import csv

class CSVFileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    # Добавление строки в файл
    def add_row(self, row_data):
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(row_data)

    # Чтение файла
    def read_file(self):
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                print(row)

    # Удаление строки в файл
    def delete_row_by_index(self, index):
        lines = []
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            lines = list(reader)

        if len(lines) > index:
            del lines[index]

        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(lines)

csv_manager = CSVFileManager('new.csv')
csv_manager.add_row(['Новая строка'])
csv_manager.add_row(['Новая строка'])
csv_manager.add_row(['Новая строка'])
csv_manager.read_file()
csv_manager.delete_row_by_index(2)