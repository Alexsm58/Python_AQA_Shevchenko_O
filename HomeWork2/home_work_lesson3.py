import random
import math

#задача 1
min = random.randrange(0, 59)
min_empty = ''
print(min)
if min >= 0 and min <= 15:
    print('First quarter')
elif min >= 16 and min <= 30:
    print('Second quarter')
elif min >= 31 and min <= 45:
    print('Third quarter')
elif min >= 46 and min <= 59:
    print('Fourth quarter')
else:
        print('Incorrect value')


#задача 2
birth_month = int(input('enter the month of your birthday: '))
if birth_month > 0 and birth_month <= 3:
    print('Snow fell outside the window')
elif birth_month >=4 and birth_month <= 6:
    print('Everything around blossomed')
elif birth_month >= 7 and birth_month <= 9:
    print('The children enjoyed their summer vacation')
elif birth_month >= 10 and birth_month <= 12:
    print('Everything around lit up with bright colors')
else:
    if birth_month <= 0:
        print('Incorrect month data')



#задача 3
random_number = str(random.randrange(1000))
print(type(random_number))
print('Random number', random_number)
if len(random_number) <= 4:
    digits = [int(digit) for digit in random_number]
    print("Individual numbers:", digits)
digit_sum = sum(int(digit) for digit in str(random_number))
print(type(digit_sum))
print("Digit sum", digit_sum)
if int(random_number) % 6 == 0 and digit_sum % 3 == 0:
    print('Congratulations!')
else:
    print('Good luck!')


#задача 4
x_coordinate = float(input('Pleas enter x coordinate: '))
y_coordinate = float(input('Pleas enter y coordinate: '))
if x_coordinate > 0 and y_coordinate > 0:
    print('First quarter of coordinates')
elif x_coordinate < 0 and y_coordinate > 0:
    print('Second quarter of coordinates')
elif x_coordinate < 0 and y_coordinate < 0:
    print('Third quarter of coordinates')
elif x_coordinate > 0 and y_coordinate < 0:
    print('Fourth quarter of coordinates')
elif x_coordinate == 0 and y_coordinate == 0:
    print('Point at origin')
else:
    if x_coordinate > 0 or x_coordinate < 0 and y_coordinate == 0:
        print('The point lies on the coordinate axis x')
    elif x_coordinate == 0 and y_coordinate > 0 or y_coordinate < 0:
        print('The point lies on the coordinate axis y')
    else:
        print('Incorrect data entered')

