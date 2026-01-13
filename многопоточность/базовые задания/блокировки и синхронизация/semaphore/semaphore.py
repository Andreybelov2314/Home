import threading
import time
database_connections = []
max_connections = 3
connection_semaphore = threading.Semaphore(max_connections)

def database_query(query_id):
    print(f'Запрос {query_id}: Ожидание соединения...')

    with connection_semaphore:  # Автоматический acquire/release
        print(f'Запрос {query_id}: Соединение установлено. Выполняю запрос...')
        # Имитация работы с БД
        time.sleep(1)
        print(f'Запрос {query_id}: Запрос выполнен.')


# Создаем запросы к базе данных
queries = []
for i in range(10):
    t = threading.Thread(target=database_query, args=(i,))
    t.start()
    queries.append(t)

# Ожидаем завершения
for q in queries:
    q.join()

print("Все запросы выполнены.")