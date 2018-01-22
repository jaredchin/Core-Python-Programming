class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return '%d:%d' % (self.hr, self.min)

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

    __repr__ = __str__



mon = Time60(10, 30)
tue = Time60(11, 15)

mon += tue

print(mon)