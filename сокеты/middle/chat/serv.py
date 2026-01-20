import socket
import threading
def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8989))
    s.listen(5)
    rooms={'python':'',
           'java':''}
    messg={'python': {},
           'java':{}}
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        rooms[data.split(',')[0]]=rooms.get(data.split(',')[0])+data.split(',')[1]
        room=data.split(',')[0]
        for k,v in messg.items():
            if room==k:
                v[data.split(',')[1]]=[data.split(',')[2]]
        print(f'пользователь {data.split(",")[1]} обработан')
        conn.close()
        print(rooms)
        print(messg)


