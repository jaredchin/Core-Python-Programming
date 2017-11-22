
alist = []
for i in range(1,101):
    alist.append(i)

hangshu = 3
#
lieshu = int(len(alist)/hangshu)
# lastlieshu = lieshu + len(alist) % hangshu
# print(lieshu, lastlieshu)



for i in range(0, len(alist)):
    if (i+1)%lieshu == 0 and (i+1)/lieshu != hangshu:
        print(alist[i])
    else:
        print(alist[i],end="")