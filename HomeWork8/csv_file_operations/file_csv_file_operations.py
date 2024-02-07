import csv

def dict_csv():

    with open('file.txt', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            print(row, type(row))
        print(csv_reader, type(csv_reader))
dict_csv()

def dict_csv_writer():
    with open('write.csv', 'w') as write_list:
        write_list = csv.writer(write_list, delimiter=',')
        write_list.writerow(['name','surname','age'])
        write_list.writerows([['Djon','Kirbi',37],['Amanda','Street',41]])

dict_csv_writer()