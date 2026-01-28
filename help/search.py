import csv
import time
import re

with open('C:\\Users\\andre\\Documents\\переломы-работа.csv', 'r', encoding='utf-8', newline='') as f:
    data = csv.DictReader(f)
    goals = []
    for i in data:
        date = i.get('Дата поступления')
        if date:
            date1 = date.split()[0]
            date2 = date1.replace('.', '/')
            year = date2.split('/')[-1]
            if year in ['23', '2023']:
                goals.append(i)
with open('C:\\Users\\andre\\Documents\\переломы-2023.csv', 'w', encoding='utf-8', newline='') as f:
    if goals:
        fieldnames = goals[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(goals)


