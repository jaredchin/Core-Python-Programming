import re
from time import ctime
f = open('redata.txt', 'r')


for eachLine in f.readlines():
    m = re.search('(\w{3}\s{1,2}\d{1,2})\s\d\d:\d\d:\d\d\s(\d{4})', eachLine)
    print('%s, %s' % (m.group(1), m.group(2)))

f.close()