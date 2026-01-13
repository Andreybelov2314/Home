import threading
import time
num=0
condition = threading.Condition()
flag=False
def worker1(condition):
    global num, flag
    while True:
        with condition:
            print('поток 1 ждет своей очереди')
            while flag==False:
                condition.wait()
            num+=1
            print(f'поток 1 отработал, {num}')
            flag=False
            condition.notify()
def worker2(condition):
    global num, flag
    while True:
        with condition:
            print('поток 2 ждет своей очереди')
            while flag==True:
                condition.wait()
            num+=0.5
            print(f'поток 2 отработал, {num}')
            flag=True
            condition.notify()
def main():

    t1=threading.Thread(target=worker1, args=(condition,))
    t2=threading.Thread(target=worker2, args=(condition,))
    t2.start()
    time.sleep(1)
    t1.start()

main()


