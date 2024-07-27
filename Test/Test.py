import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {elapsed_time:.4f} секунд")
        return result
    return wrapper
