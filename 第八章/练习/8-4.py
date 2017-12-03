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


print(isprime(num))
