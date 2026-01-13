import csv
import threading
from two_files_classes import *
data1=[]
data2=[]

lock=threading.Lock()
def work_with_csv(filename):
    global data1
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for i in reader:
            nm=i['Name']
            dp=i['Department']
            sl=i['Salary']
            obj=work_csv(nm,dp,sl)
            data1.append(obj)
        with lock:
            print('csv файл обработан')
def work_with_txt(filename):
    global data2
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.readlines()
        for i in data:
            n=i.split(';')[0]
            a=i.split(';')[1]
            c=i.split(';')[2]
            obj=work_txt(n,a,c)
            data2.append(obj)
        with lock:
            print('txt файл обработан')
def cat(filename):
    global data1, data2
    new_data = []

    header = ['name', 'age', 'city', 'department', 'salary']
    new_data.append(header)
    for i in data1:
        new_upd=[]
        for j in data2:
            if i.nm==j.give_name:
                new_upd=[i.nm,j.birthday,j.home,i.work,i.sal_info]
                new_data.append(new_upd)
    with lock:
        print('файлы соеденены')
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerows(new_data)
    with lock:
        print('файл записан')
def worker():
    t1=threading.Thread(target=work_with_csv, args=('C:\\Users\\andre\\Documents\\Py_files\\данные.csv',))
    t2=threading.Thread(target=work_with_txt, args=('C:\\Users\\andre\\Documents\\Py_files\\cat_file.txt',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3=threading.Thread(target=cat, args=('C:\\Users\\andre\\Documents\\Py_files\\сводные_данные.csv',))
    t3.start()
    t3.join()
    print('все)')
worker()












