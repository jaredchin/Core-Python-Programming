import random


def createfile(value, count, len):
    ls = []
    n = len - count
    for i in range(n):
        ran = random.randint(0, 255)
        if ran != value:
            ls.append(chr(ran))
        elif ran == value and value == 0:
            ran = random.randint(1, 255)
            ls.append(chr(ran))
        elif ran == value and value == 255:
            ran = random.randint(0, 254)
            ls.append(chr(ran))
        elif ran == value:
            ran = random.randint(0, value - 1)
            ls.append(chr(ran))
    for i in range(count):
        ls.insert(random.randint(0, n), chr(value))
    f = open(r'test.txt', 'wb')
    f.write(''.join(ls))
    f.close()


createfile(97, 3, 50)
f = open(r'test.txt', 'rb')
for i in f:
    print(i)
f.seek(0, 0)
print(len(f.readlines()[0]))

f.close()