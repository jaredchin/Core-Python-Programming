from functools import reduce
import time

def timeit(func, *args, **kwargs):
    try:
        startime = time.time()
        print(startime)
        result = func(*args, **kwargs)
        stoptime = time.time()
        print(stoptime)
        usetime = stoptime - startime
    except Exception as e:
        return 'Error'
    return result, usetime


def mult(x, y):
    return x * y

N = 5
Njiecheng = reduce(mult, list(range(1, N+1)))
print(Njiecheng)


Njiecheng1 = reduce(lambda x, y: x * y, list(range(1, N+1)))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))

print(timeit(factorial, 800))