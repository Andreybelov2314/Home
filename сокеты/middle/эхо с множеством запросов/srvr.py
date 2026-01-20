import socket
import time

def srv():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8888))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('сервер подключен')
        data=conn.recv(1024).decode('utf-8')
        new_data=data.upper()
        conn.send(new_data.encode('utf-8'))





