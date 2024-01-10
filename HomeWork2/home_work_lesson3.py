import random
import math

#задача 1
min = random.randrange(0, 59)
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
birth_month = int(input('enter the month of your birthday'))
if birth_month > 0 and birth_month <= 3:
    print('Snow fell outside the window')
elif birth_month >=4 and birth_month <= 6:
    print('Everything around blossomed')
elif birth_month >= 7 and birth_month <= 9:
    print('The children enjoyed their summer vacation')
elif birth_month >= 10 and birth_month <= 12:
    print('Everything around lit up with bright colors')
else:
    print('Incorrect month data')

'''
#задача 3
random_number = random.randrange(1000)
print(random_number)
digit_sum = sum(int(digit) for digit in str(random_number))
if random_number % 2 == 0 and digit_sum % 3 == 0:
    print("That's the right number")
else:
    print("Sorry, that's the wrong number")

random_number = random.randrange(1000)
print(random_number)
string_length = len()
#digit_sum = sum(int(digit) for digit in str(random_number))
if random_number % 6 == 0 and len(random_number(2)):
    print("That's the right number")
else:
    print("Sorry, that's the wrong number")
'''

#задача 4
x_coordinate = int(input('Pleas enter x coordinate'))
y_coordinate = int(input('Pleas enter y coordinate'))
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
