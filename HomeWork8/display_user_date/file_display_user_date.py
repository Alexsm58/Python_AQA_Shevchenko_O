import re

#завдаеея 4
def extract_dates(filename):
    dates_list = []

    with open(filename, 'r') as file:
        for line in file:
            #Regular expression for searching dates in the format "number word year"
            pattern = r'(\d{1,2}\w{0,2}\s\w+\s\d{4})'
            # Пошук дати у рядку
            match = re.search(pattern, line)
            if match:
                #If a date is found, add it to the list as a dictionary
                date = match.group(1)
                dates_list.append({"date": date})

    return dates_list

#Call function with file name "authors.txt"
result = extract_dates("authors.txt")
print(result)