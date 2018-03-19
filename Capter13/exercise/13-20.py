class Time60(object):
    def __init__(self, hr=0, min=0):
        self.hr = hr
        self.min = min
        if hr < 10:
            self.fhr = '0' + str(hr)
        else:
            self.fhr = str(hr)
        if min < 10:
            self.fmin = '0' + str(min)
        else:
            self.fmin = str(min)

    def __str__(self):
        return '%s:%s' % (self.fhr, self.fmin)

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

    __repr__ = __str__



mon = Time60()
tue = Time60(11, 5)

mon += tue

print(tue)