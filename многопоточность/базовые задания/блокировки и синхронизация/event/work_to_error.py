import time
import threading
import random
lock = threading.Lock()
event = threading.Event()
total=0
time_error=[5,5,4,3,5]
def worker1(name):
    global total
    print(f'поток {name} ожидает...')
    while True:
        event.wait()
        with lock:
            total+=1
            print(f'поток {name}, total={total}')
        time.sleep(2)
def worker2(name):
    global total
    print(f'поток {name} ожидает...')
    while True:
        event.wait()
        with lock:
            total +=0.1
            print(f'поток {name}, total={total}')
        time.sleep(2)
def worker3(name):
    global total
    print(f'поток {name} ожидает...')
    while True:
        event.wait()
        with lock:
            total += 0.5
            print(f'поток {name}, total={total}')
        time.sleep(2)
def commander():
    global time_error
    while True:
        work=random.choice(time_error)
        if work==3:
            print('на сервере зафиксированна ошибка')
            event.clear()
            time.sleep(5)
            print('ошибка исправлена')
        else:
            event.set()
            event.clear()
        time.sleep(1)
t1=threading.Thread(target=worker1, args=('w1',))
t2=threading.Thread(target=worker2, args=('w2',))
t3=threading.Thread(target=worker3, args=('w3',))
t4=threading.Thread(target=commander)
t1.start()
t2.start()
t3.start()
t4.start()

