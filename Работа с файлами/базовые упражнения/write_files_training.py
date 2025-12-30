import csv
import json

upd=[
    'milk',
    'apples',
    'bread'
]
with open('C:\\Users\\andre\\Documents\\Py_files\\wishlist.txt', 'w', encoding='utf-8') as f:
    f.writelines(upd)
    f.close()
with open('C:\\Users\\andre\\Documents\\Py_files\\wishlist.txt', 'w', encoding='utf-8') as f:
    f.write('Список покупок \n')
    for i in upd:
        f.write(i+'\n')
    f.close()
with open('C:\\Users\\andre\\Documents\\Py_files\\numbers.txt', 'w', encoding='utf-8') as f:
    for i in range(101):
        f.write(str(i) + '\n')
    f.close()
with open('C:\\Users\\andre\\Documents\\Py_files\\contacts.csv', 'w', encoding='utf-8') as f:
    fn=['имя','телефон','почта']
    datas=[        {'имя': 'Иван Иванов', 'телефон': '+79161234567', 'почта': 'ivan@mail.ru'},
        {'имя': 'Мария Петрова', 'телефон': '+79037654321', 'почта': 'maria@gmail.com'}]
    writer = csv.DictWriter(f, fieldnames=fn)
    writer.writeheader()
    writer.writerows(datas)
    f.close()
with open('C:\\Users\\andre\\Documents\\Py_files\\contacts.csv', 'r', encoding='utf-8') as f:
    con=f.read()
print(con)
print('-==============-')
with open('C:\\Users\\andre\\Documents\\Py_files\\multiplication_table.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 10):
        upd = ''
        for j in range(1, 10):
            res = int(i) * int(j)
            if len(str(res)) == 1:
                upd += str(res) + '  '
            elif len(str(res)) == 2:
                upd += str(res) + ' '
        f.write(upd+"\n")
with open('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.txt', 'r', encoding='utf-8') as f:
    ex=''
    for line in f.readlines():
        if int(line.split(',')[2])>80:
            ex+=line+'\n'
with open('C:\\Users\\andre\\Documents\\Py_files\\Ex_students.txt', 'w', encoding='utf-8') as f:
    for i in ex.split('\n'):
        f.write(i+'\n')
with open('C:\\Users\\andre\\Documents\\Py_files\\user_data.json', 'w', encoding='utf-8') as f:
    while True:
        upd={}
        info=input('введите имя')
        info2=input('введите город')
        info3=input('введите возраст')
        upd['name']=info
        upd['city']=info2
        upd['phone_number']=info3
        f.write(json.dumps(upd, ensure_ascii=False, indent=3))
        dec=input('продолжить: да или нет')
        if dec=='нет':
            break
with open('C:\\Users\\andre\\Documents\\Py_files\\user_data.json', 'r', encoding='utf-8') as f:
    data=json.load(f)
print(data)
