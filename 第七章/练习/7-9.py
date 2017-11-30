
def tr(srcstr, dststr, string, lowup=0):
    if lowup == 1:
        srcstr = srcstr.lower()
        dststr = dststr.lower()
        string = string.lower()
        return string.replace(srcstr, dststr)
    else:
        return string.replace(srcstr, dststr)


print(tr('Abc', 'Mno', 'abcDef', lowup=1))


