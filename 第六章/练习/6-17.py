def myPop(alist):
    m = alist[len(alist)-1]
    alist = alist[:len(alist)-1]
    print(alist)
    return m

aalist = [1, 2,3, 4, 5]
print(myPop(aalist))