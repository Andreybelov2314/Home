import csv
import socket
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024).decode('utf-8')
        data = eval(data)
        if data[1] == 'csv':
            with open(data[0], 'r', encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                conn.send(str(list(reader)).encode('utf-8'))
        elif data[1] == 'txt':
            with open(data[0], 'r', encoding='utf-8') as f:
                conn.send(str(f.read()).encode('utf-8'))