import json
def to_dct(data):
    dct=[]
    for i in data.split('\n'):
        upd={}
        upd['name']=i.split(',')[0]
        upd['subject']=i.split(',')[1]
        upd['result']=i.split(',')[2]
        dct.append(upd)
    return dct
with open('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.txt', 'r', encoding='utf-8') as f:
    conten=f.read()
with open('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.json', 'w', encoding='utf-8') as f:
    data=to_dct(conten)
    f.write(json.dumps(data, ensure_ascii=False, indent=4))
with open('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.json', 'r', encoding='utf-8') as f:
    data=json.loads(f.read())
print(data)

