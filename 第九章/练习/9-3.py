filename = input('Please input the filename you want to see: ')

f = open(filename, 'r')
lines = 0
for eachLine in f:
    lines += 1

print(lines)