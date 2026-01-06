import threading
dct={}
lock=threading.Lock()
threads=[]
def update():
    with lock:
        key=input('введите ключ')
        val=input('введите значение')
        global dct
        dct[key]=val
    return 'в словарь добавлен новый элемент'
def worker():
    global dct,threads
    while True:
        dec=input('продолжить работу со словарем или заврешить?')
        if dec=='-1':
            return dct
        else:
            t=threading.Thread(target=update)
            threads.append(t)
            t.start()
            t.join()
print(worker())
print(threads)


