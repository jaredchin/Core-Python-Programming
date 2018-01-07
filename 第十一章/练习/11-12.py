import time

def timeit(func, *args, **kwargs):
    try:
        startime = time.time()
        result = func(*args, **kwargs)
        stoptime = time.time()
        usetime = stoptime - startime
    except Exception as e:
        return 'Error'
    return result, usetime


def timetest(a):
    b = 0
    for i in range(a):
        time.sleep(0.5)
        b += i
    return b

print(timeit(timetest, 1))