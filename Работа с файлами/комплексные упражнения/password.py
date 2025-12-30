import random
import re
def password(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        data2 = re.split(r"[., \n:]", data)
        while True:
            first_part=random.choice(data2)
            if len(first_part)>=3:
                break
        while True:
            second_part=random.choice(data2)
            if len(second_part)>=3 and len(first_part)+len(second_part)<=10 and len(first_part)+len(second_part)>=8:
                break
        res=first_part+second_part
        return res
print(password('C:\\Users\\andre\\Documents\\Py_files\\password.txt'))


