astring = 'abcdefghijklmnopqrstuvwxyz'
bstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

srcstr = input('Input your string: ')
dststr = ''
for i in srcstr:
    if i in astring + bstring:
        for j in range(0, len(astring)):
            if astring[j] == i:
                if 0 <= j < 13:
                    dststr += astring[j + 13]
                else:
                    dststr += astring[j - 13]
            elif bstring[j] == i:
                if 0 <= j < 13:
                    dststr += bstring[j + 13]
                else:
                    dststr += bstring[j - 13]
    else:
        dststr += i

print(dststr)

