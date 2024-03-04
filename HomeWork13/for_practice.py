import csv

#завдання 5



def dict_csv():
    #read file 'new_file.csv'
    with open('new_file.csv') as reade_new_file:
        new_csv_file = csv.reader(reade_new_file,delimiter=',')
        for items in new_csv_file:
            print(items)

dict_csv()

def rewrite_funk():
    #first wrote everything to file 'new_file.csv' then rewrote it to file 'write.csv', adding lines
    with open('write.csv', 'w', newline='') as new_file:    #added a parameter newline='' so that there is no empty line
        new_file = csv.writer(new_file,delimiter=',')
        new_file.writerows([['Max','Ann','Alex'],['Stefan2','Druu','Dthochua'],['Stefan3','Druu','Dthochua']])
        new_file.writerows([['New','Row','Test'],['Second','Row','Test']])  #rewrote it to file 3 adding lines

rewrite_funk()