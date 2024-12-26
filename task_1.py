import time
import random
import threading
import multiprocessing

# Функция для вычисления интеграла
def monte_carlo_integral(f, a, b, n):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        total += f(x)
    return (b - a) * total / n

def f(x):
    return x**2

# Последовательная версия
def sequential_version():
    a = 0
    b = 1
    n = 10000000

    start_time = time.time()
    result = monte_carlo_integral(f, a, b, n)
    end_time = time.time()

    print(f"Последовательный результат: {result}")
    print(f"Время выполнения: {end_time - start_time:.4f} секунд")

# Многопоточная версия
def threaded_version():
    def monte_carlo_integral_thread(f, a, b, n, result, index):
        total = 0
        for _ in range(n):
            x = random.uniform(a, b)
            total += f(x)
        result[index] = (b - a) * total / n

    a = 0
    b = 1
    n = 10000000
    num_threads = 4
    results = [0] * num_threads
    threads = []

    start_time = time.time()

    for i in range(num_threads):
        thread = threading.Thread(target=monte_carlo_integral_thread, args=(f, a, b, n // num_threads, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_result = sum(results) / num_threads
    end_time = time.time()

    print(f"Многопоточный результат: {final_result}")
    print(f"Время выполнения: {end_time - start_time:.4f} секунд")

def worker(f, a, b, n):
    return monte_carlo_integral(f, a, b, n)

# Многопроцессорная версия
def multiprocess_version():
    a = 0
    b = 1
    n = 10000000
    num_processes = multiprocessing.cpu_count()

    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        tasks = [(f, a, b, n // num_processes)] * num_processes
        results = pool.starmap(worker, tasks)

    final_result = sum(results) / num_processes
    end_time = time.time()

    print(f"Многопроцессорный результат: {final_result}")
    print(f"Время выполнения: {end_time - start_time:.4f} секунд")

if __name__ == "__main__":
    print("Запуск последовательной версии:")
    sequential_version()
    print("\nЗапуск многопоточной версии:")
    threaded_version()
    print("\nЗапуск многопроцессорной версии:")
    multiprocess_version()