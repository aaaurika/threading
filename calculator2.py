import threading
import random
import time

def fill_file(file_path, event):
    with open(file_path, 'w') as f:
        for _ in range(100):
            number = random.randint(1, 1000)
            f.write(f"{number}\n")
            time.sleep(0.01)  # Симулируем работу
    event.set()

def find_primes(file_path, event, output_file):
    event.wait()
    primes_count = 0
    with open(file_path, 'r') as f, open(output_file, 'w') as out:
        for line in f:
            number = int(line.strip())
            if is_prime(number):
                primes_count += 1
                out.write(f"{number}\n")
    print(f"Найдено простых чисел: {primes_count}")

def calculate_factorial(file_path, event, output_file):
    event.wait()
    with open(file_path, 'r') as f, open(output_file, 'w') as out:
        for line in f:
            number = int(line.strip())
            out.write(f"{number}! = {factorial(number)}\n")
    print(f"Вычислено факториалов: {len(output_file)}")

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")
    event = threading.Event()


    thread_fill = threading.Thread(target=fill_file, args=(file_path, event))
    thread_primes = threading.Thread(target=find_primes, args=(file_path, event, "primes.txt"))
    thread_factorial = threading.Thread(target=calculate_factorial, args=(file_path, event, "factorials.txt"))


    thread_fill.start()
    thread_primes.start()
    thread_factorial.start()


    thread_fill.join()
    thread_primes.join()
    thread_factorial.join()

    print("Статистика операций:")
    print(f"Файл '{file_path}' заполнен.")
    print(f"Результаты поиска простых чисел записаны в 'primes.txt'.")
    print(f"Результаты вычисления факториалов записаны в 'factorials.txt'.")