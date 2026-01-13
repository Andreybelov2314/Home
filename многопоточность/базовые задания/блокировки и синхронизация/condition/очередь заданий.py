import threading
import time
import random
from collections import deque
total=0
tasks=[]
rt=[3,4,5,5,5,6,7,3,10,10,10]
condition=threading.Condition()
flag=True
lock=threading.Lock()
def task_maker(cond):
    global tasks, total, flag
    while total!=10:
        with condition:
            while flag==False:
                condition.wait()
            for i in range(3):
                tasks.append([f'task {i}'])
                print(f'task {i}-добавлена')
                time.sleep(3)
            print('список задач полный')
            flag=False
            condition.notify()
def tasks_worker(cond):
    global tasks, total, rt, flag
    while total!=10:
        with condition:
            while flag==True:
                condition.wait()
            for i in tasks:
                tme=random.choice(rt)
                time.sleep(tme)
                print(f'задача {i} решена')
            tasks=[]
            total+=1
            flag=True
            condition.notify()


def main():
    t1=threading.Thread(target=task_maker, args=(condition,))
    t2=threading.Thread(target=tasks_worker, args=(condition,))
    t1.start()
    t2.start()
main()