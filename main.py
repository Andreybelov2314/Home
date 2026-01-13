import csv

with open('C:\\Users\\andre\\Documents\\Py_files\\сводные_данные.csv', 'r', encoding='utf-8', newline='') as f:
    reader=csv.DictReader(f)
    for i in reader:
        print(i)
