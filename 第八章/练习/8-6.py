num = int(input('Input a num: '))

def isprime(num):
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True

def getfactors(num):
    alist = []
    for i in range(2, num+1):
        if num % i == 0:
            alist.append(i)
        else:
            continue
    return alist

def getlist(num):
    alist = []
    blist = []
    for i in getfactors(num):
        if isprime(i):
            alist.append(i)
    for j in alist:
        while True:
            blist.append(j)
            num = num / j
            if num % j == 0:
                continue
            else:
                break
    return blist

print(getlist(num))



