import random
import math

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
if int(random_number) % 6 == 0 and int(digit_sum) % 3 == 0:
    print('Congratulations!')
else:
    print('Good luck!')
