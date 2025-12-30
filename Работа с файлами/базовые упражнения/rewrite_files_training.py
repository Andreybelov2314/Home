'''upd=[
    'milk',
    'apples',
    'bread'
]
with open('C:\\Users\\andre\\Documents\\Py_files\\wishlist.txt', 'w', encoding='utf-8') as f:
    for i in upd:
        f.write(i+'\n')
with open('C:\\Users\\andre\\Documents\\Py_files\\wishlist.txt', 'a', encoding='utf-8') as f:
    f.writelines('кофе'+'\n')
    f.writelines('сахар')'''
import time
def log_message():
    text=input('введите сообщение')
    tm=time.localtime()
    return f'{text}, {tm}'
with open('C:\\Users\\andre\\Documents\\Py_files\\log.txt', 'a', encoding='utf-8') as f:
    upd=log_message()
    f.write(upd+'\n')


