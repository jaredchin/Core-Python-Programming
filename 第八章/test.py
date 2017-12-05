myFile = open('config-win.txt')

for eachLine in myFile:
    print(eachLine, end='')

myFile.close()