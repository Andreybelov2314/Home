import threading
from сокеты.base.пример import client, server
import time
def main():
    t1=threading.Thread(target=server.server)
    t2=threading.Thread(target=client.client)
    t1.start()
    print('сервер ждет...')
    time.sleep(2)
    t2.start()
    t1.join()
    t2.join()
    print('программа завершена')
main()