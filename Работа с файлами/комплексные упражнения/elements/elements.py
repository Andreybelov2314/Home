from class_elem import *
total=[]
with open('C:\\Users\\andre\\Documents\\Py_files\\elements.txt', 'r', encoding='utf-8') as f:
    data=f.readlines()
for i in data:
    obj=elements(i.split(' ')[0], i.split(' ')[1], i.split(' ')[2], i.split(' ')[3])
    total.append(obj)
while True:
    name=input('введите название элемента ')
    if name=='-1':
        break
    for i in total:
        if i.element_name==name:
            print(i.get_info())

