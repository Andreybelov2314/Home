import threading
import time
def incrementer(counter, condition, stop_event):
    """
    Поток, который увеличивает счетчик.

    Args:
        counter: общая переменная счетчика
        condition: объект Condition для синхронизации
        stop_event: флаг остановки работы
    """
    while not stop_event.is_set():  # Работаем, пока не получим сигнал остановки
        with condition:  # Автоматически захватываем и освобождаем condition
            # Ждем, пока счетчик меньше 5. Используем while, а не if
            while counter >= 5:
                print("Увеличитель: Достигнут максимум (5), жду...")
                condition.wait()  # Освобождаем блокировку и ждем

            # Увеличиваем счетчик
            counter += 1
            print(f"Увеличитель: счетчик = {counter}")

            # Уведомляем все ожидающие потоки
            condition.notify_all()

        # Небольшая пауза для наглядности
        time.sleep(0.3)

    print("Увеличитель: Завершил работу")


def decrementer(counter, condition, stop_event):
    """
    Поток, который уменьшает счетчик.

    Args:
        counter: общая переменная счетчика
        condition: объект Condition для синхронизации
        stop_event: флаг остановки работы
    """
    while not stop_event.is_set():  # Работаем, пока не получим сигнал остановки
        with condition:  # Автоматически захватываем и освобождаем condition
            # Ждем, пока счетчик больше 0. Используем while, а не if
            while counter <= 0:
                print("Уменьшитель: Достигнут минимум (0), жду...")
                condition.wait()  # Освобождаем блокировку и ждем

            # Уменьшаем счетчик
            counter -= 1
            print(f"Уменьшитель: счетчик = {counter}")

            # Уведомляем все ожидающие потоки
            condition.notify_all()

        # Небольшая пауза для наглядности
        time.sleep(0.2)

    print("Уменьшитель: Завершил работу")


def main():
    """Основная функция программы."""
    # Создаем общие переменные
    counter = 0  # Наш счетчик, начальное значение 0
    condition = threading.Condition()  # Создаем объект Condition
    stop_event = threading.Event()  # Создаем событие для остановки

    print("=== Программа Синхронизированный Счетчик ===")
    print("Условия: 0 <= счетчик <= 5")
    print("Работа программы: 10 секунд\n")

    # Создаем и запускаем потоки
    inc_thread = threading.Thread(
        target=incrementer,
        args=(counter, condition, stop_event),
        name="Увеличитель"
    )

    dec_thread = threading.Thread(
        target=decrementer,
        args=(counter, condition, stop_event),
        name="Уменьшитель"
    )

    # Запускаем потоки
    inc_thread.start()
    dec_thread.start()

    # Даем потокам поработать 10 секунд
    print("Программа работает 10 секунд...\n")
    time.sleep(10)

    # Подаем сигнал остановки
    print("\nПодаем сигнал остановки...")
    stop_event.set()

    # Ждем завершения потоков
    inc_thread.join()
    dec_thread.join()

    print("\nОба потока завершили работу")
    print(f"Финальное значение счетчика: {counter}")
main()