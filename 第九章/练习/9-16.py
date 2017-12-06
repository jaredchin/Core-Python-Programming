import os

content = []
f = open(r'9-16.txt', 'r')
lines = f.readlines()
f.close()

for line in lines:
    if len(line) <= 80:
        content.append(line)
    else:
        words = line.strip().split()
        sum = 0
        l = ''
        for w in words:
            w += ' '
            sum += len(w)
            if sum < 80:
                l += w
            else:
                content.append(l)
                l = w
                sum = len(w)
        else:
            content.append(l)
            l = ''

f = open(r'9-16.txt', 'w')
for item in content:
    f.write(item + '\n')
f.close()