import socket
def server1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8080))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        data=conn.recv(1024)
        if not data:
            break
        data=data.decode('utf-8')
        res=int(data)+2
        conn.send(str(res).encode('utf-8'))
    conn.close()