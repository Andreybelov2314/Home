import threading
import client_game
import server_game
import time

flag = False

def main():
    cond = threading.Condition()
    t1 = threading.Thread(target=server_game.server, args=(cond,))
    t2 = threading.Thread(target=client_game.client, args=(cond,))
    t1.start()
    time.sleep(2)
    t2.start()
if __name__ == '__main__':
    main()

