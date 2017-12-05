f = open('9-5.txt', 'r')
aList = []
for eachLine in f:
    a = int(eachLine.strip())
    aList.append(a)

f.close()

zf = 0
for i in aList:
    zf += int(i)
print(zf/len(aList))