charname = chr(int(input('Please input a number of chr: ')))
filename = input('Please input the filename: ')

f = open(filename,'r')
num = 0
lines = f.readlines()
for line in lines:
    for ch in line:
        if ch == charname:
            num += 1
        else:
            pass

print(num)