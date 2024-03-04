import csv
import json


class JSONConverter:
    def __init__(self):
        self.lines = []

    def read_file(self, filename):
        with open(filename, 'r') as json_file:
            self.lines = json.load(json_file)

    def write_file(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.lines[0].keys())
            for line in self.lines:
                writer.writerow(line.values())
        self.cleanup()

    def cleanup(self):
        self.lines = []


converter = JSONConverter()

# Преобразование первого JSON файла в CSV
converter.read_file('example.json')
converter.write_file('example.csv')

# Преобразование второго JSON файла в CSV
converter.read_file('example.json')
converter.write_file('example_second.csv')
