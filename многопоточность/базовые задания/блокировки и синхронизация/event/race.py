import threading
import time
import random
event = threading.Event()
start_event=threading.Event()
time_race=[3,4,5,3,4,2,1]
res={}
lock=threading.Lock()
def car(nam):
    global time_race, res
    with lock:
        print(f'автомобиль {nam} к старту готов')
    start_event.wait()
    with lock:
        print(f'автомобиль {nam} стартовал')
    rt=random.choice(time_race)
    res[nam]=rt
    with lock:
        print(f'автомобиль {nam}-{rt} секунды')
def referee():
    with lock:
        print('на старт')
    time.sleep(1)
    print('внимание')
    time.sleep(1)
    print('марш')
    time.sleep(1)
    start_event.set()
cars = []
for i in range(1, 6):
    car_thread = threading.Thread(target=car, args=(i,))
    car_thread.start()
    cars.append(car_thread)
judge_thread = threading.Thread(target=referee())
judge_thread.start()
for car_thread in cars:
    car_thread.join()

print("\nГонка завершена!")
print(res)


