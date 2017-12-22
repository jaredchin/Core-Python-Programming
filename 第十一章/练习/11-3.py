

def max2(a,b):
    if a > b:
        return a
    else:
        return b

def my_max(alist):
    if len(alist) == 0:
        return 'Can not be None'
    else:
        res = alist[0]
        for i in alist:
            res = max2(res, i)
        return res

alist = [1,2,3,4,5,6,7]
print(my_max(alist))
