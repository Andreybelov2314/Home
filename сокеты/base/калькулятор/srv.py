import socket
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)
    conn, addr = sock.accept()
    while True:
        data=conn.recv(1024).decode('utf-8')
        if data=='-1':
            break
        start=0
        if data[0]=='-':
            upd='-'
        else:
            upd='+'
        for i in data:
            if i.isalnum():
                upd+=i
            else:
                if upd[0]=='-':
                    start-=int(upd[1:])
                    upd=str(i)
                elif upd[0]=='+':
                    start+=int(upd[1:])
                    upd=str(i)
                elif upd[0]=='*':
                    start*=int(upd[1:])
                    upd=str(i)
                elif upd[0]=='/':
                    start/=int(upd[1:])
                    upd=str(i)

        conn.send(f'{data}{start}'.encode('utf-8'))
    conn.close()

