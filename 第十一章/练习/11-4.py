

def minTohour(minu):
    hour = minu / 60
    minute = minu % 60
    return '%d hour %d minute' % (hour, minute)


print(minTohour(100))