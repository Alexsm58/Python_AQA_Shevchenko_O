import csv

with open('birthday.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
    print(csv_reader, type(csv_reader))
csv_file.close()

with open('birthday.txt','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

with open('birthday.csv', 'w') as birthday:
    birthday_writer = csv.writer(birthday, delimiter=',')
    birthday_writer.writerow(['name','surname','group','birthday'])
    birthday_writer.writerow(['Jon','Dow','python',5])
    birthday_writer.writerows([['Sam', 'Beck', 'backend',7], ['Hanna','Houk','hrr',0]])
    for row in birthday:
        print(birthday)

with open('birthday2.csv', 'w') as birthday:
    birthday_headers = ['name','surname','group','birthday']
    birthday_dict_writer = csv.DictWriter(birthday, fieldnames=birthday_headers)
    birthday_dict_writer.writeheader()
    birthday_dict_writer.writerow({'name':'Jonatan','surname':'Calm','group':'python','birthday':5})