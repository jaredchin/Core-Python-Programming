f = open('9-6.txt', 'r')
f1 = open('9-61.txt', 'r')

flist = []
f1list = []
for eachLinef in f:
    flist.append(eachLinef)

for eachLinef1 in f1:
    f1list.append(eachLinef1)

for i in range(len(flist)):
    if flist[i] == f1list[i]:
        pass
    else:
        print('第 ', i+1 ,' 行')
        break

for j in range(len(flist[i])):
    if flist[i][j] == f1list[i][j]:
        pass
    else:
        print('第 ', j+1 ,' 列 不一样')
        break