import csv
import json
import pathlib
import collections

path = "C:\\Users\\Erik\Code\\neos\\cd0010-advanced-python-techniques-project-starter\\data"

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

with open(f'{path}\\neos.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)
    count = 0
    for row in reader:
        count += 1
    print(f'NEO Count = {count}')

cad = load_json(f'{path}\\cad.json')
cad_count = 0
for entry in cad:
    print(entry)
    if entry == 'data':
        for line in entry:
            cad_count += 1
print(f'Cad Count = {cad_count}')

