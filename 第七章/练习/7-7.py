adict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
bdict = {}

for key in adict:
    bdict[adict[key]] = key

print(bdict)
