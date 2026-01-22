import threading
import socket
import random
def client():
    lock=threading.Lock()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))
    num=[1,2,3,4,5,6,7,8,9,10]
    signs=['+','-','*','/']
    n1=random.choice(num)
    n2=random.choice(num)
    sign=random.choice(signs)
    sock.send(f'{n1}{sign}{n2}'.encode('utf-8'))
    data = sock.recv(1024).decode('utf-8')
    with lock:
        print(data)
    sock.close()
