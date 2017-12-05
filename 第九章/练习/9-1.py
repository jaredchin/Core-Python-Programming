

f = open('9-1.txt', 'r')
for eachLine in f:
    if len(eachLine.strip()) == 0:
        print(eachLine, end='')
    elif eachLine.strip()[0] == '#':
        pass
    else:
        print(eachLine, end='')
