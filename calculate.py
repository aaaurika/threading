import threading
import random
import time

def fill_list(numbers, event):
    for _ in range(10):
        numbers.append(random.randint(1, 100))
        time.sleep(0.1)
    event.set()

def calculate_sum(numbers, event):
    event.wait()
    print(f"Сумма элементов: {sum(numbers)}")

def calculate_mean(numbers, event):
    event.wait()
    print(f"\nСреднеарифметическое: {sum(numbers) / len(numbers)}")

if __name__ == "__main__":
    numbers = []
    event = threading.Event() 

    # Создаем потоки
    thread_fill = threading.Thread(target=fill_list, args=(numbers, event))
    thread_sum = threading.Thread(target=calculate_sum, args=(numbers, event))
    thread_mean = threading.Thread(target=calculate_mean, args=(numbers, event))

    # Запускаем потоки
    thread_fill.start()
    thread_sum.start()
    thread_mean.start()

    # Ожидаем завершения работы потоков
    thread_fill.join()
    thread_sum.join()
    thread_mean.join()

    print("Список:", numbers)
