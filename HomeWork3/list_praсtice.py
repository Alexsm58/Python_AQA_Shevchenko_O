first_list = [1, 3, 2, 5, 4, 9, 8, 7, 6]
#first_list.sort()
#print(first_list)
#print(sorted(first_list))
#print(sorted(first_list, reverse = True))
second_list = first_list[:4]
print(second_list[:4])
print(first_list[4:])
print(first_list[2:5])    # с 2 по 5(5-й не включно)
first_list.extend((second_list))    #конкотинація двух списків(добавили другий список до першого)
print(first_list)
for elemtnt in first_list:
    print(elemtnt*2)

a = [1, 2, 3, 4]
b = a
a.append(5)
print(a)
print(b)
b.append(6)
print(b)
c = a.copy()    # cкопіює усе
c.pop()     # pop видаляє останній єлемент
print(c)
d = list(a)     #ще один варіант створити копію
print('Print d', d)
a.pop()
print(a)
print(d)

first_tuple = (1, 2, 3, 4, 5, 6, 7)
#print(first_tuple[0])
for elemtnt in first_tuple:
    elemtnt = elemtnt**2
    print(elemtnt)
print(elemtnt)

new_list = [1, 3, 6, 8, 10]
element_list = []
for elemtnt in new_list:
    if elemtnt > 6:
        element_list.append(elemtnt)
print(element_list)

counter = 0
while counter < 10:
    print('you have write counter')
    counter += 2

for i in 'Hallo World':
    if i == 'o':
        continue    #continue буде крутитись до тих пір поки не закінчиться цикл
    print(i)
''' 
while counter < 20:
    counter += 1
    if counter%2 == 1:
        continue
    print(counter)
'''
while counter < 30:
    counter += 1
    if counter %2 == 1:
        print('I`m about o break')
        break    #break брутально обрубить
    print(counter)

entered = 0
while True:
    new_entered = input('Enter a number or sum: ')
    if new_entered == 'sum':
        print(entered)
        break
    elif new_entered.startswith('-') and new_entered[1:] or new_entered.isnumeric():
        entered += int(new_entered)
    else:
        print('Not a number')

