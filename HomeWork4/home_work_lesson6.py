import math
import random

#завдання 1
def find_the_same(list1, list2):
    #finding identical data in lists
    set_list1 = set(list1)
    set_list2 = set(list2)
    same_set = set_list1.intersection(set_list2)    #we are looking for the same data in the lists
    return sorted(list(same_set))   #we return the sorted result of the same

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
def random_dict_items(name_list, surname_list, location_list):
    #Randomly displays values in dictionaries from lists
    name = random.choice(list(name_list))
    surname = random.choice(list(surname_list))
    location = random.choice(list(location_list))
    return{'name': name, 'surname': surname, 'location': location}

name_list = ['Alex', 'Alesha', 'Sasha', 'Mariia', 'Gena', 'Kateryna']
surname_list = ['Williams', 'Stud', 'Zeus', 'Brown', 'Taylor', 'Jackson']
location_list = ['Colorado', 'Florida', 'Idaho', 'Indiana']

final_dict = random_dict_items(name_list, surname_list, location_list)
print(final_dict)
