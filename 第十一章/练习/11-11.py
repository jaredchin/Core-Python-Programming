
f = open('test.txt', 'r')
newcont = map(lambda x: x.strip(), f.readlines())
f1 = open('test1.txt', 'w')
for cont in newcont:
    f1.write(cont + '\n')

f.close()
f1.close()