import time
import threading
import random
lock = threading.Lock()
class rocket():
    def __init__(self, number, time_starting, status):
        self.number = number
        self.time_starting = time_starting
        self.status = status
    @property
    def name(self):
        return self.number

    @name.setter
    def name(self, value):
        self.number = value
    @property
    def time(self):
        return self.time_starting

    @time.setter
    def time(self, value):
        self.time_starting = value
    @property
    def stat(self):
        return self.status

    @stat.setter
    def stat(self, value):
        self.status = value
roc=[]
rs=[3,5,4,6,7,7,7,7,8,7,8]
for i in range(3):
    obj = rocket(i+1, random.choice(rs), 'готовится')
    roc.append(obj)
print(roc)


def worker(barrier, obj):
    print(f'ракета {obj.name} начинает подготовку')
    time.sleep(obj.time)
    obj.stat='готова'
    print(f'{obj.name}-{obj.stat}')
    barrier.wait()
    time.sleep(3)
    obj.stat='полетела'
    with lock:
        print(f'{obj.name}-{obj.stat}')
threads=[]
barrier=threading.Barrier(3)
for i in roc:
    t=threading.Thread(target=worker, args=(barrier, i))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print('все ракеты улетели')




