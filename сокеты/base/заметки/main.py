import threading
import socket
import clt
import srv
import time
def main():
    lock=threading.Lock()
    t1=threading.Thread(target=srv.server, args=(lock,))
    t2=threading.Thread(target=clt.clt, args=(lock,))
    t1.start()
    time.sleep(4)
    t2.start()
    t1.join()
    t2.join()
    time.sleep(3)
    print('работа программы завершена')
main()
