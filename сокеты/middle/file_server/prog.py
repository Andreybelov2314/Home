from cln import *
from srv import *
import threading
import time
def main():
    t1=threading.Thread(target=server)
    t1.start()
    time.sleep(2)
    t2=threading.Thread(target=cln)
    t2.start()
main()