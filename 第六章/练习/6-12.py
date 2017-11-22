def findchr(astring, achar):
    for i in range(0, len(astring)):
        if astring[i] == achar:
            return i
    else:
        return -1

print(findchr('abcdea', 'e'))


def rfindchr(astring, achar):
    for i in range(-len(astring)+1, 0):
        if astring[i] == achar:
            return(i+len(astring))
    else:
        return -1
print(rfindchr('abcdea', 'e'))


def subchr(astring, achar, bchar):
    bstring = ''
    for i in range(0, len(astring)):
        if astring[i] == achar:
            bstring = bstring + bchar
        else:
            bstring = bstring + astring[i]
    return bstring

print(subchr('abcdea', 'b', 'z'))
