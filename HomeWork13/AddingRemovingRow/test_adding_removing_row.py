import csv

class TestCSV():
    #завдання 2
    def test_add_row(self):
        #opening the file for reading
        with open('new.csv', 'r') as file:
            lines_before = file.readlines()

        #add one line to the file
        with open('new.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Stefanko","Jacek","Jaryna"])

        #checking the number of lines after adding
        with open('new.csv', 'r') as file:
            lines_after = file.readlines()

        #checking if the number of rows has increased by one using an assert statement
        assert len(lines_after) == len(lines_before) + 1
        print("The number of lines has increased by one")

    def test_remove_row(self):

        with open('new.csv', 'r') as file:
            lines_before = file.readlines()

        with open('new.csv', 'r') as file:
            lines = file.readlines()

        #removing the penultimate line from the list
        del lines[-1]

        #rewrite the file with the remaining lines
        with open('new.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows([line.strip().split(',') for line in lines])

        #checking that the line has been deleted
        with open('new.csv', 'r') as file:
            lines_after_remove = file.readlines()

        assert len(lines_after_remove) == len(lines_before) - 1
        print('line was successfully deleted')

#creating a class instance and calling test methods
tester = TestCSV()
tester.test_add_row()
tester.test_remove_row()
