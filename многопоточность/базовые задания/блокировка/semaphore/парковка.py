import time
import threading
import random
semaphore=threading.Semaphore(5)
total=5
lock=threading.Lock()
stopped=[3,4,5,1,1,1,2,3]
def upd_total():
    global total
    with lock:
        total+=1
def down():
    global total
    with lock:
        total-=1
def worker(quercy_id):
    global total, stopped
    print(f'машина с номером {quercy_id} пытается заехать на парковку')
    with semaphore:
        print(f'машина с номером {quercy_id} заехала на парковку')
        down()
        print(f'количество свободных мест-{total}')
        slp_time=random.choice(stopped)
        time.sleep(slp_time)
        print(f'машина с номером {quercy_id} выехала с парковки')
        upd_total()
        print(f'количество свободных мест-{total}')
queries=[]
for i in range(10):
    t=threading.Thread(target=worker, args=(i,))
    t.start()
    queries.append(t)
for q in queries:
    q.join()
print('все машины уехали')