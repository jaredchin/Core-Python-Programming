import re
from time import ctime
f = open('redata.txt', 'r')
lines = f.readlines()
f.close()

email = 'qinzuode@qinzuode.qinzuode'
f1 = open('redata1.txt', 'w')


for eachLine in lines:
    m = re.split('::', eachLine)
    newline = '%s::%s::%s' % (m[0], email, m[2])
    f1.write(newline)


f1.close()