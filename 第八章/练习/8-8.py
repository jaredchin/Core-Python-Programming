num = int(input('Input a num: '))


def factorial(num):
    a = 1
    for i in range(1, num+1):
        a *= i
    return a

print(factorial(num))