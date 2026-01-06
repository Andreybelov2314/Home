import csv

with open('C:\\Users\\andre\\Documents\\Py_files\\employees.csv', 'r', encoding='utf-8', newline='') as f:
    data = csv.DictReader(f)
    res = {}

    for i in data:
        sub = i.get('subjects')
        marks = i.get('scores')
        subjects_list = sub.split(',')
        marks_list = marks.split(',')
        for l in range(len(subjects_list)):
            subject = subjects_list[l]
            mark = marks_list[l] if l < len(marks_list) else None
            if subject not in res:
                res[subject] = [int(mark)] if mark else []
            else:
                if mark:
                    res[subject].append(int(mark))
sub_info={}
for k,v in res.items():
    total=0
    for c in v:
        total+=c
    upd=total/len(v)
    sub_info[k] = upd
print(sub_info)


