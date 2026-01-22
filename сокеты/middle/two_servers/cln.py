import socket
import threading
def client(num):
    lock = threading.Lock()
    s = socket.socket()
    s.connect(('127.0.0.1', 8080))
    s.send(str(num).encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    with lock:
        print(f'сервер 1 отработал, результат-{data}')
    s.close()
    s2=socket.socket()
    s2.connect(('127.0.0.1', 9090))
    s2.send(str(data).encode('utf-8'))
    data2=s2.recv(1024).decode('utf-8')
    with lock:
        print(f'сервер 2 отработал, результат-{data2}')
    s2.close()
