import json
with open('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.txt', 'r', encoding='utf-8') as f:
    conten=f.read()
    print(conten)
    f.seek(0)
    str1=f.readlines()
    print(len(str1))
    f.close()
print('-==========-')
data=[
  {
    "title": "Мастер и Маргарита",
    "author": "Михаил Булгаков",
    "year": 1967,
    "pages": 480
  },
  {
    "title": "Преступление и наказание",
    "author": "Фёдор Достоевский",
    "year": 1866,
    "pages": 672
  },
  {
    "title": "1984",
    "author": "Джордж Оруэлл",
    "year": 1949,
    "pages": 328
  }
]
with open("C:\\Users\\andre\\Documents\\Py_files\\my_data.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()
print('-==========-')
with open("C:\\Users\\andre\\Documents\\Py_files\\my_data.json", 'r', encoding='utf-8') as f:
    data=json.load(f)
    f.close()
print('-==========-')
with open('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.txt', 'r', encoding='utf-8') as f:
    content=f.readlines()
    f.close()
for i in content:
    upd=''
    upd+=i.split(',')[0]+','
    upd+=i.split(',')[2]
    if int(i.split(',')[2])>90:
        upd+='отлично'
    elif int(i.split(',')[2])>80:
        upd+='хорошо'
    else:
        upd+='плохо'
    print(upd)
print('-==============-')
def mmm(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        info=f.readlines()
        f.close()
    marks=[]
    for i in info:
        marks.append(int(i.split(',')[2]))
    return f'{max(marks)}, {min(marks)}, {sum(marks)/len(marks)}'
print('-===========-')
with open("C:\\Users\\andre\\Documents\\Py_files\\my_data.json", 'r', encoding='utf-8') as f:
    data=json.load(f)
    f.close()
titles=[]
pages=0
books=[]
for i in data:
    for k,v in i.items():
        if k=='title':
            titles.append(v)
        elif k=='pages':
            pages+=int(v)
        elif k=='year' and int(v)>1900:
            books.append(i)
print(titles)
print(pages)
print(books)
print('-================-')
