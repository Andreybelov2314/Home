import socket
from cls_worker import *
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024).decode('utf-8')
        obj=worker(data)
        res=obj.complete()
        conn.send(f'{res}'.encode('utf-8'))
        conn.close()