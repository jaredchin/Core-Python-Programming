aList = input('输入多个成绩用逗号(,)间隔: ').split(',')

zf = 0
for i in aList:
    zf += int(i)
print(zf/len(aList))