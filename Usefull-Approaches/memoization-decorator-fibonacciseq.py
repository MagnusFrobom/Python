def use_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@use_cache
def fibbonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonacci(n - 1) + fibbonacci(n - 2)


print(fibbonacci(8))