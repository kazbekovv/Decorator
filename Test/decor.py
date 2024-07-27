from Test import timing_decorator
import time

@timing_decorator
def slow_function():
    time.sleep(2)  # Имитация долгой работы

if __name__ == "__main__":
    slow_function()




