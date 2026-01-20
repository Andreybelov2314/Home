import socket
def clt(lock):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))
    while True:
        with lock:
            comm=input('введите команду')
        sock.send(comm.encode('utf-8'))
        if comm=='exit':
            break
        elif comm=='lst':
            data=sock.recv(4096).decode('utf-8')
            print(data)
        elif comm=='add':
            upd=input('введите заметку')
            sock.send(upd.encode('utf-8'))
            sock.recv(1024)