aList = input('输入多个数字用逗号(,)间隔: ').split(',')
bList = []
for i in aList:
    i = int(i)
    bList.append(i)
bList.sort(reverse=True)
print(tuple(bList))
aList.sort(reverse=True)
print(aList)