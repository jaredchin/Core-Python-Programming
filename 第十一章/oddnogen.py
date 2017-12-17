from random import randint
# def odd(n):
#     return n % 2

allNums = []

for eachNum in range(9):
    allNums.append(randint(1, 99))

fil = filter(lambda x: x % 2, allNums)
print(list(fil))


print([n for n in [randint(1, 99) for i in range(9)] if n % 2])

