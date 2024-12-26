import requests
import threading
import multiprocessing
import time

urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.bbc.com",
]


def fetch_url(url):
    response = requests.get(url)
    print(f"URL: {url}, Код ответа: {response.status_code}")


# Последовательное выполнение
def sequential_fetch():
    print("Запуск последовательного выполнения...")
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    end_time = time.time()
    print(f"Время последовательного выполнения: {end_time - start_time:.2f} секунд\n")


# Поточное выполнение
def threaded_fetch():
    print("Запуск поточного выполнения...")
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Время поточного выполнения: {end_time - start_time:.2f} секунд\n")


# Процессное выполнение
def process_fetch():
    num_cores = multiprocessing.cpu_count()
    print("Запуск процессного выполнения...")
    start_time = time.time()
    with multiprocessing.Pool(processes=num_cores) as pool:
        pool.map(fetch_url, urls)
    end_time = time.time()
    print(f"Время процессного выполнения: {end_time - start_time:.2f} секунд\n")


if __name__ == "__main__":
    sequential_fetch()

    threaded_fetch()

    process_fetch()
