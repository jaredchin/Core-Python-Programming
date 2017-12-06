import os

fobj = open('test.txt', 'w')
while True:
    aLine = input("Enter a line ('.' to quit): ")
    if aLine != ".":
        fobj.write('%s\n' % aLine)
    else:
        break

fobj.close()