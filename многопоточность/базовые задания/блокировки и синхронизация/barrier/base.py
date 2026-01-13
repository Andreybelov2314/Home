import threading
import time
import random
def worker(barrier, name):
    print(f"{name} начинает подготовку...")
    time.sleep(random.uniform(0.5, 2))
    print(f"{name} готов к старту")

    # Ждем всех у барьера
    barrier.wait()

    print(f"{name} стартовал!")


# Создаем барьер для 3 потоков
barrier = threading.Barrier(3)

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(barrier, f"Участник {i + 1}"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()