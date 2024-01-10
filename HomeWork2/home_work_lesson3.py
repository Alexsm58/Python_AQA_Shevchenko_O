import random

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
