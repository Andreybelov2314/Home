import csv
#после прочтения csv.DictReader(f) исчерпан, надо создавать новый
def class_best(filename):
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        data=csv.DictReader(f)
        clas_dct={}
        for i in data:
            if i['grade'] not in clas_dct.keys():
                clas_dct[i['grade']] = [i['scores']]
            elif i['grade'] in clas_dct.keys():
                upd=list(clas_dct.get(i['grade']))
                upd.append(i['scores'])
                clas_dct[i['grade']] = upd
    mc=''
    mmm=0
    for k in clas_dct:
        nmm=0
        mq=0
        for v in clas_dct[k]:
            for c in v.split(','):
                mq+=1
                nmm+=int(c)
            res=nmm/mq
            if res>mmm:
                mc=k
                mmm=res
    return f'лучший класс-{mc}, {mmm}'
print(class_best('C:\\Users\\andre\\Documents\\Py_files\\employees.csv'))