import re

def extract_dates(filename):
    dates_list = []

    # Відкриття файлу для читання
    with open(filename, 'r') as file:
        # Прочитати рядки з файлу
        for line in file:
            # Регулярний вираз для пошуку дати у форматі "число слово рік"
            pattern = r'(\d{1,2}\w{0,2}\s\w+\s\d{4})'
            # Пошук дати у рядку
            match = re.search(pattern, line)
            if match:
                # Якщо знайдено дату, додати її до списку у вигляді словника
                date = match.group(1)
                dates_list.append({"date": date})

    return dates_list

# Виклик функції з ім'ям файлу "authors.txt"
result = extract_dates("authors.txt")
print(result)