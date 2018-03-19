from re import match
f = open('redata.txt', 'r')


count = 0

for eachLine in f.readlines():
    m = match('^Fri', eachLine)
    if m is not None:
        count += 1

print(count)

f.close()