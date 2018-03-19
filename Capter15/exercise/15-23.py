import re
from time import ctime
f = open('redata.txt', 'r')


for eachLine in f.readlines():
    m = re.search('\d\d:\d\d:\d\d', eachLine)
    print(m.group())

f.close()