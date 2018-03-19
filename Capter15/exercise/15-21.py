import re
from time import ctime
f = open('redata.txt', 'r')


for eachLine in f.readlines():
    m = re.match('[A-Z][a-z]{2}\s([A-Z][a-z]{2})', eachLine)
    print(m.group(1))

f.close()