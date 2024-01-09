import math   #імпорт бібліотеки math
import random   #імпорт бібліотеки random
a = 1
#b = id(a)
print(id(a))   #викликати id-шнік

b = 2.5
print(id(b))
print(type(b))

c = 'text'
print(type(c))
d = False
print(type(d))   #виликати тип функції


simple_int = "Oleksandr"
second_int = "Shevchenko"
third_int = 5.1


print(simple_int + " " + second_int)
print(third_int)
print(third_int-1)
print(third_int+1)
print(third_int/2)
print(type(third_int))
print(8//2)
print(10%3)

f = 5
g = 2.5
c = f + g
print(c)
print(type(c))

first_float = 5.747634354
print(round(first_float, 6))    #roundокруглення до 'n' знаків після коми
print(dir(math))

print(math.pi)

print(dir(random))   #dir викликає атрібути обєкта

print(random.randint(10, 40))   #random.randint - рандотізуе в проміжку між 10 та 40
print(random.randrange(50))   #random.randrang - рандотізуе в проміжку між 0 та 50
print(random.choice(['black', 'white', 'green']))   #random.choice - рандотізуе між значеннями які вписані в []
print(random.choice([10, 15]))


message = "i`m a new message"   #корегування регістром букв в строках
print(message.capitalize())
print(message.title())
print(message.lower())
print(message.upper())


first_name = 'Oleksandr'
last_name = 'Shevchenko'
full_name = '\t'+first_name+' '+last_name   #\t - табуляція
print(full_name)


print('students:\nOlha\nVolodymyr') #\n - перенос строки

print('      python'.lstrip())  #strip прибирає пробіли l/s+strip зліва або зправа
print('Python       '.rstrip())
print('    Python    '.strip())

print('Python is a very bad language'.replace('bad', 'good'))   #replace - замена текста в строке
print('Python is a very bad language'.replace('P', 'p'))


print('bad' in 'Python is a very bad language') # in - перевіряемо чи є bad' в тексті далі
print('good' in 'Python is a very bad language')

py_string_example = 'Python is a very bad language'
print('bad' in py_string_example)   # in - перевіряемо чи є bad' в тексті далі
print('good' in py_string_example)

print(py_string_example.islower())  #islower перевіряє в якому регістрі строка
print(py_string_example.startswith('Python'))   #startswith перевіряє слово на початку речення
print(py_string_example.endswith('lan'))    #startswith перевіряє слово на початку речення

print(py_string_example.count('bad'))   #count скільки разів bad є в тексті
print(py_string_example.index('bad'))   #літера В в строці 17 за індексом
print(py_string_example.find('bat'))    #find шукає слово bat в стоці

splitted_string = py_string_example.split()   #split розділяє строку на єлементи
print(splitted_string)

splitted_string = py_string_example.split(' a ')    #split розділяє строку на до та після 'а'
print(splitted_string)

lines_example = 'a\n b\n c'
print(lines_example.splitlines())   #splitlines порубали строку на окремі секції

print(py_string_example[0])   #витягнули індекс 0 це Р в строці 'Python is a very bad language'

food = 'Pizza'
cost = 150

str_cost = str(cost)
print(type(str_cost))
print('Your' + ' ' + "foood" + ' ' + "coast" + ' ' + str_cost)
print('Thenks for this {}, this is your {}'.format(food, cost))   #format вставив нам необхідні змфннф у текст
print(f'Happily, I went home with my {food}, fnd without my {cost} hryvnias')   #f швидка та простіша вставка формату