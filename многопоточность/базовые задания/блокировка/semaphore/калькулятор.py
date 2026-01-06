import time
import random
import threading
r_time=[1,2,3]
lock=threading.Lock()
semaphore=threading.Semaphore(3)
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
signs=['+','-','*']
def worker():
    global r_time,signs,num
    first=random.choice(num)
    sign=random.choice(signs)
    second=random.choice(num)
    print(f'{first}{sign}{second}=?')
    with semaphore:
        if sign=='*':
            ts=random.choice(r_time)
            time.sleep(ts)
            print(f'{first}{sign}{second}={first*second}')
        elif sign=='+':
            ts=random.choice(r_time)
            time.sleep(ts)
            print(f'{first}{sign}{second}={first+second}')
        elif sign=='-':
            ts=random.choice(r_time)
            time.sleep(ts)
            print(f'{first}{sign}{second}={first-second}')
quories=[]
for i in range(10):
    t=threading.Thread(target=worker,args=())
    t.start()
    quories.append(t)
for t in quories:
    t.join()
print('вычисления завершены')
