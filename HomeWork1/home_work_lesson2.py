import math

#завдання 1
first_name = 'oleksandr'
last_name = 'shevchenko'
full_name = first_name+' '+last_name

print(full_name)
print(full_name.lower())
print(full_name.upper())
print(first_name.capitalize()+' '+last_name.capitalize())

change_name = '    oleksandr    '
print(change_name)
print('\t\noleksandr\t\n')
print('\t\noleksandr\t\n'.strip())
print(change_name.strip())


#завдання 2
radius = 6
circle_length = 2*math.pi*radius
print(f'circle length is {circle_length}')
area_of_a_circle = math.pi*radius**2
print(f'area of a circle is {area_of_a_circle}')


#задание 3
dollar_exchange_rate = 38.4828
amount_equal_to_a_dollar = 1000
amount_equal_to_a_dollar = float(dollar_exchange_rate)
print(amount_equal_to_a_dollar.__round__(2))
