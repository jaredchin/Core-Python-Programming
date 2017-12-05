

filename = input('Please input the filename you want to see: ')
lines = int(input('How many lines you want to see ? '))

f = open(filename, 'r')
for i in range(0, lines):
    print(f.readline(), end='')