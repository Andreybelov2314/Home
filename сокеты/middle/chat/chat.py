from clien import *
from serv import *
import threading
import socket
import time
def main():
    t1=threading.Thread(target=server)
    t1.start()
    time.sleep(1)
    for i in range(5):
        t=threading.Thread(target=clnt, args=(i,))
        t.start()
        time.sleep(1)
main()
