import re
def head_copy(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.readlines()
        for i in data[0:4]:
            print(i)
    return ''
def tail_copy(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.readlines()
        for i in data[-4:-1]:
            print(i)
    return ''

def str_num(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.readlines()
    with open("C:\\Users\\andre\\Documents\\Py_files\\stud_num.txt", 'w', encoding='utf-8') as f:
        num=1
        for i in data:
            f.write(f'{num}:{i}')
            num+=1
"""def cat(file1, file2):
    res=''
    with open(file1, 'r', encoding='utf-8') as f:
        data=f.readline()
        res+=str(data)+'\n'
    with open(file2, 'r', encoding='utf-8') as f:
        data=f.readline()
        res+=str(data)+'\n'
    with open("C:\\Users\\andre\\Documents\\Py_files\\cat_file.txt", 'w', encoding='utf-8') as f:
        f.writelines(res)"""
def max_word(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.read()
        data2=re.split(r"[.,:\n ]", data)
        ml=0
        mw=''
        for i in data2:
            if len(i)>ml:
                mw=str(i)+','
                ml=len(i)
            elif len(i)==ml and i not in mw.split(','):
                mw+=str(i)
    return f'максимальная длинна слова-{ml}-{mw}'
print(max_word('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.txt'))
def letters_fr(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.read()
        res={}
        for i in data:
            i=i.lower()
            if i.isalpha() and i not in res.keys():
                res[i]=data.count(i)
    return res
print(letters_fr('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.txt'))



