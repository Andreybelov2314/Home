import random
import socket
import threading
import игра
def server(condition):
    sock = socket.socket()
    sock.bind(('', 5665))
    sock.listen()
    conn, addr = sock.accept()
    words=['взгляд', 'землеройка', 'виселица', 'футбол', 'медведь']
    rw=random.choice(words)
    conn.send(rw.encode('utf-8'))
    while True:
        with condition:
            while игра.flag==False:
                condition.wait()
            word_str=conn.recv(1024)
            word_str=word_str.decode('utf-8')
            hit=''
            for i in range(len(rw)):
                if rw[i]==word_str:
                    hit+=str(i)
            if len(hit)==0:
                hit='-1'
            conn.send(hit.encode('utf-8'))
            игра.flag=False
            condition.notify()



