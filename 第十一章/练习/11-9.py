from functools import reduce


def average(alist):
    sumlist = reduce(lambda x, y: x + y, alist)
    return sumlist / len(alist)


alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(average(alist))