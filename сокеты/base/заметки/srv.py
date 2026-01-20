import socket
def server(lock):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)
    lst=[]
    conn, addr = sock.accept()
    with lock:
        print('сервер подключен')
    while True:
        command=conn.recv(1024).decode('utf-8')
        if command=='exit':
            break
        elif command=='lst':
            conn.send(f'{lst}'.encode('utf-8'))
        elif command=='add':
            data=conn.recv(1024).decode('utf-8')
            lst.append(data)
            conn.send('ok'.encode('utf-8'))
    conn.close()

