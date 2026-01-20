import socket
import time
def client():
    sock=socket.socket()
    sock.connect(('localhost',8080))
    while True:
        comm=input('введите пример')
        sock.send(comm.encode('utf-8'))
        res=sock.recv(1024).decode('utf-8')
        print(res)
        time.sleep(2)

