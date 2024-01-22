import math
import random

#завдання 1
def find_the_same(list1, list2):
    #Функцію для знаходження однакових данних в списках
    set_list1 = set(list1)
    set_list2 = set(list2)
    same_set = set_list1.intersection(set_list2)    #шукаємо однакові данні у списках
    return sorted(list(same_set))   #повертаємо вже відсортований результат однакових даних з типом list

list1 = [12, 10, 9, 6, 4, 2]
list2 = [12, 11, 9, 7, 5, 4]

results = find_the_same(list1, list2)
if len(results) >= 1:
    print(f'These are the common values in the lists {results}')
else:
    print('There are no matches yet')


#завдання 2
def student_performance():
    #The program determines the score requirements
    students_scores = {
    'sasha':7,
    'tolik':7,
    'igor':10,
    'Slava':8,
    'Anna':10,
    'Voitek':7
}

    #Calculate the average score
    average_score = sum(students_scores.values()) / len(students_scores)
    #Print the names of students with scores above the average
    print('Students with scores above the average:')
    for name, value in students_scores.items():
        if value > average_score:
            print(f'{name.title()}:{value}')

student_performance()


#завдання 3
def random_dict_items(name, surname, location):
    #Randomly displays values in dictionaries from lists
    name(name_list)
    surname(surname_list)
    location(location_list)
    return
name_list = ['Alex', 'Alesha', 'Sasha', 'Mariia', 'Gena', 'Kateryna']
surname_list = ['Williams', 'Stud', 'Zeus', 'Brown', 'Taylor', 'Jackson']
location_list = ['Colorado', 'Florida', 'Idaho', 'Indiana']

name = random.choice(list(name_list))
surname = random.choice(list(surname_list))
location = random.choice(list(location_list))

finali_dict = {'name': name, 'surname': surname, 'location': location}
print(finali_dict)