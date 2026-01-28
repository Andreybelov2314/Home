import csv
with open('C:\\Users\\andre\\Documents\\переломы-2023-дубликаты_.csv', 'r', encoding='utf-8', newline='') as f:
    data = list(csv.DictReader(f))
    goals = []
    processed_names = []
    for i in data:
        upd = i
        name = i.get('ИНП')
        if name in processed_names:
            continue
        with open('C:\\Users\\andre\\Documents\\переломы-2023-дубликаты_.csv', 'r', encoding='utf-8', newline='') as f2:
            for j in csv.DictReader(f2):
                if j.get('ИНП') == name:
                    date1 = i.get('Дата поступления')
                    date = date1.split()[0]
                    date2 = date.replace('.', '/')
                    date_parts_i = date2.split('/')
                    num = j.get('Дата поступления')
                    num1 = num.split()[0]
                    num2 = num1.replace('.', '/')
                    num_parts = num2.split('/')
                    year_i = date_parts_i[-1][-2:]
                    year_j = num_parts[-1][-2:]
                    if int(year_j) > int(year_i):
                        upd = i
                    elif int(year_j) < int(year_i):
                        upd = j
                    else:
                        if int(num_parts[-2]) > int(date_parts_i[-2]):
                            upd = i
                        elif int(num_parts[-2]) < int(date_parts_i[-2]):
                            upd = j
                        else:
                            if int(num_parts[-3]) > int(date_parts_i[-3]):
                                upd = i
                            elif int(num_parts[-3]) < int(date_parts_i[-3]):
                                upd = j
                            else:
                                upd = i
            goals.append(upd)
            processed_names.append(name)
with open('C:\\Users\\andre\\Documents\\переломы-уникальные.csv', 'w', encoding='utf-8', newline='') as f:
    if goals:
        fieldnames = goals[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(goals)

