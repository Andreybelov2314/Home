import threading
lock = threading.Lock()
total=1000
threads=[]
def update(itaritions):
    global total
    for _ in range(itaritions):
        with lock:
            total += 1
    return total
def worker(iterations):
    for i in range(10):
        t=threading.Thread(target=update, args=(iterations,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return total

print(worker(1000))

