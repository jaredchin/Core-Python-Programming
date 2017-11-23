adict = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(sorted(adict))

for key in sorted(adict):
    print('key %s has value %s' % (key, adict[key]))
