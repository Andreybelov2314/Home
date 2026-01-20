
import socket
def client():
    sock = socket.socket()
    sock.connect(('localhost', 8080))
    sock.send('hello, world!'.encode('utf-8'))
    data = sock.recv(1024)
    sock.close()
    print (data)