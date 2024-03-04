import csv

# Открываем файл для чтения
with open('file.txt', 'r') as file:
    lines_before = file.readlines()
# Добавляем одну строку в файл
with open('file.txt', 'a') as file:
    file.write("Новая строка\n")
# Проверяем количество строк после добавления
with open('file.txt', 'r') as file:
    lines_after = file.readlines()
# Проверяем, увеличилось ли количество строк на одну с помощью утверждения assert
assert len(lines_after) == len(lines_before) + 1, "Ошибка: количество строк не увеличилось на одну."
print("Количество строк увеличилось на одну.")
# Открываем файл для чтения
with open('file.txt', 'r') as file:
    lines_before = file.readlines()
# Удаляем одну строку из файла (например, первую строку)
with open('file.txt', 'r') as file:
    lines = file.readlines()
with open('file.txt', 'w') as file:
    file.writelines(lines[1:])
# Проверяем количество строк после удаления
with open('file.txt', 'r') as file:
    lines_after = file.readlines()
# Проверяем, уменьшилось ли количество строк на одну с помощью утверждения assert
assert len(lines_after) == len(lines_before) - 1, "Ошибка: количество строк не уменьшилось на одну."
print("Количество строк уменьшилось на одну.")