import socket
def server():
    sock=socket.socket()
    sock.bind(('127.0.0.1',8090))
    sock.listen(2)
    conn,addr=sock.accept()
    while True:
        data=conn.recv(1024)
        if not data:
            break
        data_str=data.decode('utf-8')
        res = f'эхо-{data_str}, длина-{len(data_str)} символов'
        conn.send(res.encode('utf-8'))
    conn.close()