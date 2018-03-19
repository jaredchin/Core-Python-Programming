import re
from time import ctime
f = open('redata.txt', 'r')


for eachLine in f.readlines():
    m = re.split('::', eachLine)
    m1 = m[0]
    m2 = re.match('^\d+', m[2]).group()
    if ctime(int(m2)) == m1:
        continue
    else:
        print('The data has wrong!!!!!')
        break


f.close()