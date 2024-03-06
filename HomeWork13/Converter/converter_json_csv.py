import csv
import json

class JSONConverter:
    #завдання 1
    def __init__(self):
        self.lines = []

    def read_file(self, filename):    #read the file JSON
        with open(filename, 'r') as json_file:
            self.lines = json.load(json_file)

    def write_file(self, filename):    #write & convert to CSV file
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.lines[0].keys())
            for line in self.lines:
                writer.writerow(line.values())
        self.cleanup()

    def cleanup(self):
        self.lines = []


converter = JSONConverter()

# converting the first JSON file to CSV
converter.read_file('example.json')
converter.write_file('example.csv')

# converting the second JSON file to CSV
converter.read_file('example.json')
converter.write_file('example_second.csv')
