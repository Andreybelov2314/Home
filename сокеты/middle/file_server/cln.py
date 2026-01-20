import socket
def cln():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))
    while True:
        fl=input('введите название файла:')
        ft=input('ввидите тип файла:')
        dct=[fl,ft]
        sock.send(str(dct).encode('utf-8'))
        data=sock.recv(4024).decode('utf-8')
        print(data)