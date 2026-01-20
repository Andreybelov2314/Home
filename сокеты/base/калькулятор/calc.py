from clt import *
from srv import *
import threading
import time
def main():
    t1=threading.Thread(target=server)
    t1.start()
    time.sleep(1)
    t2=threading.Thread(target=client)
    t2.start()
main()
