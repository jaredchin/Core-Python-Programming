from random import randint, choice
from string import ascii_lowercase
from sys import maxsize
from time import ctime
from os import linesep

doms = ('com', 'edu', 'net', 'org', 'gov')
f = open('redata.txt', 'w')

for i in range(randint(5, 50)):
    dtint = randint(0, 9999999999)
    dtstr = ctime(dtint)

    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(ascii_lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(ascii_lowercase)

    line = '%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)
    f.write(line)

f.close()