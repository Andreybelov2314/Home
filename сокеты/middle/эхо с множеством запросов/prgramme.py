import socket
from clnt import cln
from srvr import srv
import threading
import time
def main():
    t1 = threading.Thread(target=srv)
    t1.daemon = True
    t1.start()
    time.sleep(2)
    while True:
        command = input('введите фразу')
        if command == '-1':
            break
        else:

            t2=threading.Thread(target=cln, args=(command,))
            t2.start()
main()