import csv
import re
with open('C:\\Users\\andre\\Documents\\ПЕРЕЛОМЫ.csv', 'r', encoding='utf-8', newline='') as f:
    data = csv.DictReader(f)
    res=[]
    for i in data:
        if i.get('Возраст')=='':
            new_patient=i
            date=re.split(r"[./]",i.get('Дата рождения'))
            day=date[0]
            month=date[1]
            year=date[2]
            if len(year) == 2:
                year = '19' + year if int(year) > 23 else '20' + year
            date2=re.split(r"[./]",i.get('Дата поступления'))
            dr=date2[0]
            mr=date2[1]
            my=date2[2]
            if len(my) == 2:
                my = '19' + my if int(my) > 23 else '20' + my
            upd=''
            if int(month)-int(mr)>0:
                upd=int(my)-int(year)
                new_patient['Возраст']=str(upd)
                res.append(new_patient)
            elif int(month)-int(mr)<0:
                upd=int(my)-int(year)-1
                new_patient['Возраст'] = str(upd)
                res.append(new_patient)
            else:
                if int(day)-int(dr)>0:
                    upd = int(my) - int(year)
                    new_patient['Возраст'] = str(upd)
                    res.append(new_patient)
                else:
                    upd = int(my) - int(year) - 1
                    new_patient['Возраст'] = str(upd)
                    res.append(new_patient)
        else:
            res.append(i)
with open('C:\\Users\\andre\\Documents\\переломы_с_возрастом.csv', 'w', encoding='utf-8', newline='') as f:
    if res:
        fieldnames = res[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(res)
print('все прошло вроде хорошо')

