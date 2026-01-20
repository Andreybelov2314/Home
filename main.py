import socket
import threading
def srv():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(1)
    conn, addr = sock.accept()
    conn.send('werty'.encode('utf-8'))
    conn.send('asdfgh'.encode('utf-8'))
    conn.close()
def cln():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8080))
    data1=sock.recv(1024).decode('utf-8')
    print(data1)
    data2=sock.recv(1024).decode('utf-8')
    sock.close()
def main():
    t1=threading.Thread(target=srv)
    t2=threading.Thread(target=cln)
    t1.start()
    t2.start()
if __name__ == '__main__':
    main()

