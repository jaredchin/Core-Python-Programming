num = int(input('Input a num: '))

def getfactors(num):
    alist = []
    for i in range(1, num+1):
        if num % i == 0:
            alist.append(i)
        else:
            continue
    return alist

print(getfactors(num))
