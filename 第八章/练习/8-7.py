num = int(input('Input a num: '))

def getfactors(num):
    alist = []
    for i in range(1, num):
        if num % i == 0:
            alist.append(i)
        else:
            continue
    return alist

def isperfect(num):
    suma = 0
    for i in getfactors(num):
        suma += i
    if suma == num:
        return True
    else:
        return False


for i in range(100):
    print(i, isperfect(i))