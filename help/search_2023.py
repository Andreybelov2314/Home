import csv
with open('C:\\Users\\andre\\Documents\\переломы-работа.csv', 'r', encoding='utf-8', newline='') as f:
    data=csv.DictReader(f)
    goals=[]
    for i in data:
        date=i.get('Дата поступления')
        if '2023' in date:
            goals.append(i)
with open('C:\\Users\\andre\\Documents\\переломы-2023.csv', 'w', encoding='utf-8', newline='') as f:
    if goals:
        fieldnames = goals[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(goals)
