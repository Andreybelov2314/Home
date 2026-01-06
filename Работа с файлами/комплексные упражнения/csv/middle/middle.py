import csv

with open('C:\\Users\\andre\\Documents\\Py_files\\employees.csv', 'r', encoding='utf-8', newline='') as f:
    data=csv.DictReader(f)
    new=[['id','name','age','grade','subjects','attendance','scores', 'average', 'status']]
    for i in data:
        upd=[]
        upd.append(i)
        marks=i.get('scores')
        marks_list = marks.split(',')
        total=0
        for f in marks_list:
            total+=int(f)
        total2=total/len(marks_list)
        upd = [
            i['id'],
            i['name'],
            i['age'],
            i['grade'],
            i['subjects'],
            i['attendance'],
            i['scores'],
            total2,
            'отличник' if total2 > 90 else ('хорошист' if total2 > 80 else 'троечник')
        ]
        new.append(upd)

with open('C:\\Users\\andre\\Documents\\Py_files\\employees.csv', 'w', encoding='utf-8', newline='') as f:
    wr = csv.writer(f)
    wr.writerows(new)

