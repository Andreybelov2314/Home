from serv2 import *
from serv1 import *
from cln import *
import threading
import time
def main():
    t1=threading.Thread(target=server1)
    t2=threading.Thread(target=server2)
    t1.start()
    t2.start()
    time.sleep(1)
    for i in range(5):
        t=threading.Thread(target=client, args=(i,))
        t.start()
        t.join()
        time.sleep(1)
main()