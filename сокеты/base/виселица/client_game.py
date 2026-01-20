import socket
import threading
import игра
def client(condition):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 5665))
    chances=6
    data1=sock.recv(1024)
    word_secret=[]
    for i in range(len(data1.decode('utf-8'))):
        word_secret.append('_')
    while True:
        with condition:
            while игра.flag==True:
                condition.wait()
            print(word_secret)
            print(f'количество жизней-{chances}')
            com=input('ввидите букву:')
            sock.send(com.encode('utf-8'))
            игра.flag=True
            condition.notify()
        with condition:
            while игра.flag==True:
                condition.wait()
            data=sock.recv(1024)
            data = data.decode('utf-8')
            if data=='-1':
                chances-=1
                print(f'буквы {com} нет, количество жизней-{chances}')
            else:
                for i in data:
                    word_secret[int(i)]=com
            if chances==0:
                break

