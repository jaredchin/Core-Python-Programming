num1 = int(input("请输入起始值:"))
num2 = int(input("请输入结束值:"))
alist = []

for i in range(num1, num2+1):
    blist = []
    blist.append(i)
    blist.append(bin(i))
    blist.append(oct(i))
    blist.append(hex(i))
    if i < 256 and i > 33:
        blist.append(chr(i))

    alist.append(blist)

if num1 in range(33, 256) or num2 in range(33, 256):
    print('十进制\t二进制\t八进制\t十六进制\tASCII')
    print('-'*50)
    for j in alist:
        for m in range(len(j)):
            print(j[m], end='')
            if m != len(j)-1:
                print('\t',end='')
            else:
                print('')
else:
    print('DEC\tBIN\tOCT\tHEX\t')
    print('-'*50)
    for j in alist:
        for m in range(len(j)):
            print(j[m],end='')
            if m != len(j)-1:
                print('\t', end='')
            else:
                print('')



