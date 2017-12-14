from urllib import request

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
    else:
        return eachLine


def firstLast(webpage):
    f = open(webpage,encoding='utf-8')
    lines = f.readlines()
    f.close()
    print(firstNonBlank(lines), end='')
    lines.reverse()
    print(firstNonBlank(lines), end='')


def download(url='http://www.renren.com', process=firstLast):
    try:
        retval = request.urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)


if __name__ == '__main__':
    download()
