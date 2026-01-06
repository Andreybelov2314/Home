import threading
import time
class MyThread:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    def increment(self):#метод для увелечения счетчика
        with self.lock:#гарантирует, что выполнять будет только 1 поток
            self.value = self.value + 1
            return self.value
    def get_value(self):
        with self.lock:
            return self.value
def worker(counter, iterations):# первое-обьект класса , который мы увеличиваем, второе-сколько раз увеличиваем
    for i in range(iterations):
        counter.increment()
res=[]
counter=MyThread()
for i in range(5):
    t = threading.Thread(target=worker, args=(counter,1000))
    res.append(t)
    t.start()
for h in res:
    h.join()
print(counter.get_value())
print(res)
