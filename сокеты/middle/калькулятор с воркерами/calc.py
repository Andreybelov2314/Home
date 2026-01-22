import threading
import time
import socket
from cls_worker import *
from cln import *
from srv import *
from сокеты.middle.file_server import cln

lock=threading.Lock()
def main():
    t1=threading.Thread(target=server)
    t1.start()
    time.sleep(2)
    for i in range(5):
        t2=threading.Thread(target=client)
        t2.start()
        time.sleep(1)
main()