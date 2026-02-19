import time

def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__}: {elapsed:.4f}s")
        return result

    return wrapper

@timer
def work():
    time.sleep(0.1)

work()
