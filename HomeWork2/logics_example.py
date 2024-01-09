new_string = 'gfjhg'
empty_string = ''
print(bool(new_string))
print(bool(empty_string))

new_value = True
falce_velue = False
print(int(new_value))
print(int(falce_velue))

a = 100
b = 200
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a==b)

# if elife else - умовні конструкції, оператори

if_value_to_reed = int(input('enter your text here'))
print(if_value_to_reed)

int_value_too_reed = input('Hi dude print int')
if int_value_too_reed.isdigit():
    print(int(int_value_too_reed))
else:
    print("It's defenitely note integer")


input_value = int(input('what is your number?'))
if input_value > 0:
    print(input_value)
else:
    print(input_value*(-1))

numbers = int(input("Tell me the numbers"))
if numbers >= 10:
    print("Your number have 2 ore more numbers")
else:
    print("Your number have 1 number")

# or and not - логычні оператори

next_imput = int(input("Hay dude print my int, please"))
if next_imput >30 or next_imput <20:
    print("Ha you'r between 20 and 30, probably")
if next_imput >200 and next_imput %20 == 0:
    print("Oh no!")
if not next_imput:
    print("Hall yeah")    #най частіше це перевірка на пусту строку (if not empty string)

str_input = input('go!')
if str_input.startswith('Hallo'):
    print('Hallo my dear')
elif str_input.isdigit():    #elif може бути багато, не рекомендується більше 5
    print('oh i see you mr robot')
else:
    print('Your typed invalid value')


#задача в складних блоках логіки
eyes = int(input('how many eyes?'))
legs = int(input('how many legs?'))
if eyes >= 8:
    if legs == 8:
        print('spider')
    elif legs == 6:
        print('cockroach')
    else:
        print('undefined creature')
else:
    if eyes == 2 and legs == 4:
        print('definitely a cat')
    else:
        print('horror beyond our comprehension')

#list - списки
cool_fruit = 'watermelon'
fruits = ['apple','banana',cool_fruit,'watermelon']
print(fruits)
print(type(fruits))
print(id(fruits))
print(len(fruits))
print(fruits[-1])
print(fruits.index('watermelon'))
fruits.append('lemon')    #append додае єлемент в кінець списку
print(fruits)
fruits.pop(1)    #pop видаляє єлемент за індексом .pop(1), або з кінця списку .pop()
print(fruits)
del fruits[1]    #можемо видаляти функцією del але це не рекомендується - це ппогана практика