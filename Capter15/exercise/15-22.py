import re
from time import ctime
f = open('redata.txt', 'r')


for eachLine in f.readlines():
    m = re.search('\s(\d{4})::', eachLine)
    print(m.group(1))

f.close()