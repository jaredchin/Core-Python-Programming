
def sum(alist, blist):
    sumlist = []
    m = len(alist)
    n = len(blist)
    for i in range(m):
        tmp = []
        for i in range(n):
            tmp.append(alist[i][j]+blist[i][j])
        sumlist.append(tmp)
    return sumlist


def matrix(alist, blist):
    malist = [[0]*len(blist[0]) for i in range(len(alist))]
    m = len(alist)
    n = len(blist[0])
    k = len(blist)
    for i in range(m):
        for j in range(n):
            for k in range(k):
                malist[i][j] += alist[i][k] * blist[k][j]
    return malist


if __name__ == '__main__':
    aalist = []
    bblist = []
    m = input()
    m = input()
    for i in range(m):
        text = input()
        text = text.split()
        aalist[i].append(text)
    m = input()
    n = input()
    for i in range(m):
        text = input()
        text = text.split()
        bblist[i].append(text)

    if (len(aalist) != len(bblist) or (len(aalist[0]) != len(bblist[0]))):
        print('行或列不相等，无法相加')
    else:
        print(sum(aalist, bblist))

    if (len(bblist) != len(aalist[0])):
        print("行与列不相等，无法相乘")
    else:
        print(matrix(aalist, bblist))