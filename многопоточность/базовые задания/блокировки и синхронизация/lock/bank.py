import threading
import time
accounts={'acc1':1000,
          'acc2':2000,
          'acc3':3000}
operation=[['acc1', 'acc3', 500], ['acc2', 'acc3', 500], ['acc3', 'acc1', 500], ['acc2', 'acc1', 100], ['acc1', 'acc2', 100], ['acc2', 'acc3', 150]]
lock=threading.Lock()
prnt_lock=threading.Lock()
def transfer(from_where, where_to, how_much):
    global accounts
    with lock:
        time.sleep(1)
        start=int(accounts.get(from_where))
        end=int(accounts.get(where_to))
        accounts[where_to]=start+int(how_much)
        accounts[from_where]=end-int(how_much)
        print(show(from_where, where_to, how_much))
def show(from_where, where_to, how_much):
    with prnt_lock:
        return f'перевод с {from_where} на аккаунт {where_to} в размере {how_much} выполнен'
def worker():
    global accounts, operation
    threads=[]
    for i in range(len(operation)):
        t=threading.Thread(target=transfer,args=(operation[i][0],operation[i][1],operation[i][2]))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    return accounts
print(worker())


