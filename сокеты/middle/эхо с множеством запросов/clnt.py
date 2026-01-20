import socket
def cln(phrase):
    sock = socket.socket()
    sock.connect(('localhost', 8888))
    sock.send(phrase.encode('utf-8'))
    data = sock.recv(1024)
    sock.close()
    print(data.decode('utf-8'))