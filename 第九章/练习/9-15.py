file1 = input('Please input the source file: ')
file2 = input('Please input the dest file: ')

f1 = open(file1, 'r')
f2 = open(file2, 'a+')

for eachLine in f1:
    f2.write(eachLine)

f1.close()
f2.close()