import threading
import socket
import random
import time
def clnt(nm):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8989))
    rr=['java', 'python']
    rc=random.choice(rr)
    sock.send(f'{rc},{nm},hello'.encode('utf-8'))
    sock.close()








