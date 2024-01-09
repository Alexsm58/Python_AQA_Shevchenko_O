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