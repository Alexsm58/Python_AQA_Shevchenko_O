#завдання 1
#виводимо однакові значення в списках
x_coordinates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '10']
y_coordinates = [7, 8, 9, 10, 11, 12, 13, 14, 15]
x_y_coordinates = list(sorted(filter(lambda x: x in x_coordinates, y_coordinates)))
print(f'Твій список однакових єлементів {x_y_coordinates}')


#завдання 2
check_string_type = lambda x: isinstance(x, str)
#перевіряємо значення в рядку на строку чи цифру
string1 = "Hello, World!"
string2 = 12345
print(check_string_type(string1))
print(check_string_type(string2))


#завдання 3
#сортування від більшого до меншого
len_list = lambda x: [len(el) for el in x]
max_list = [[0, 1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [1]]
print("Довжина вкладених списків:", len_list(max_list))
print("Мінімальний підсписок:", min(max_list))
print("Максимальний підсписок:", max(max_list))
print("Сортування списку:", sorted(max_list))


