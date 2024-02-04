#завдання 1
#we display the same values in the lists
x_coordinates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '10']
y_coordinates = [9, 8, 7, 10, 11, 12, 13, 14, 15]
x_y_coordinates = list(sorted(filter(lambda x: x in x_coordinates, y_coordinates)))
print(f'Your list of identical elements {x_y_coordinates}')


#завдання 2
#we check the value in the line for a period or a number
string1 = "Hello, World!"
string2 = 12345
check_string_type = lambda x: isinstance(x, str)
print(check_string_type(string1))
print(check_string_type(string2))


#завдання 3
#sorting from largest to smallest
max_list = [[0, 1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [1]]
len_list = lambda x: [len(el) for el in x]
print("Minimal sublist:", min(max_list))
print("Maximum sublist:", max(max_list))