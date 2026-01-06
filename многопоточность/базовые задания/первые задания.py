import threading
import time
def new_year():
    for i in range(6):
        print(i)
        time.sleep(1)

t = threading.Thread(target=new_year)
t2= threading.Thread(target=new_year)
t3= threading.Thread(target=new_year)
t.start()
t2.start()
t.join()
t2.join()