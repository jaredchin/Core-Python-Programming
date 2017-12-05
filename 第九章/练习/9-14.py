import sys


def writeline(line):
    f = open('9-14.txt', 'a')
    f.write(line)
    f.close()



def printline():
    f = open('9-14.txt', 'r')
    for i in f:
        print(i,end='')
    f.close()
    f = open('9-14.txt', 'w+')
    f.truncate()
    f.close()


args = sys.argv
if args[1] == 'print':
    printline()
    exit()


line = ''
for arg in args:
    line += arg + ' '


args[1] = float(args[1])
args[3] = float(args[3])





def caculate(args):
    if args[2] == '+':
        return args[1] + args[3]
    elif args[2] == '-':
        return args[1] - args[3]
    elif args[2] == '*':
        return args[1] * args[3]
    elif args[2] == '/':
        return args[1] / args[3]


print(caculate(args))
writeline(line + '\n')
writeline(str(caculate(args)) + '\n')
