
import csv

class TestCSVFile:
    # Строка, которую нужно добавить в файл CSV
    new_row = ['Max', 'Ann', 'Alex']

    # Имя файла CSV
    file_name = 'prakticsfile.csv.csv'

    # Открываем файл CSV в режиме добавления (a) и создаем объект writer
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Добавляем новую строку в файл CSV
        writer.writerow(new_row)

    print("Строка успешно добавлена в файл CSV.")
