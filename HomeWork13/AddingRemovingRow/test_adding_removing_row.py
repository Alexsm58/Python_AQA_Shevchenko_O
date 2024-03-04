from HomeWork13.AddingRemovingRow.adding_removing_row import CSVFileManager
import csv

class TestCSV():

    def test_add_row(self):
        # Открываем файл для чтения
        with open('new.csv', 'r') as file:
            lines_before = file.readlines()

        # Добавляем одну строку в файл
        with open('new.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Stefanko","Jacek","Jaryna"])

        # Проверяем количество строк после добавления
        with open('new.csv', 'r') as file:
            lines_after = file.readlines()

        # Проверяем, увеличилось ли количество строк на одну с помощью утверждения assert
        assert len(lines_after) == len(lines_before) + 1
        print("Количество строк увеличилось на одну.")

    def test_remove_row(self):
        # Открываем файл для чтения
        with open('new.csv', 'r') as file:
            lines_before = file.readlines()

        # Читаем все строки в список
        with open('new.csv', 'r') as file:
            lines = file.readlines()

        # Удаляем предпоследнюю строку из списка
        del lines[-1]

        # Перезаписываем файл с оставшимися строками
        with open('new.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows([line.strip().split(',') for line in lines])

        # Проверяем, что строка была удалена
        with open('new.csv', 'r') as file:
            lines_after_remove = file.readlines()

        assert len(lines_after_remove) == len(lines_before) - 1
        print("Предпоследняя строка успешно удалена.")

# Создание экземпляра класса и вызов методов тестирования
tester = TestCSV()
tester.test_add_row()
tester.test_remove_row()
