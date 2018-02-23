

# def dollarize(fcount):
#     fcount = round(fcount, 2)
#     sfcount = format(fcount, ',')
#     if fcount < 0:
#         sfcount = sfcount.split('-')[1]
#         return '-' + '$' + sfcount
#     else:
#         return '$' + sfcount

class MoneyFmt(object):
    def __init__(self, fcount):
        self.fcount = float(fcount)

    def update(self, fcount=None):
        if fcount is not None:
            try:
                self.fcount = float(fcount)
            except(TypeError) as e:
                print(e)

    def __nonzero__(self):
        return self.fcount

    def __repr__(self):
        return self.fcount

    def __str__(self):
        return self.dollarize()

    def dollarize(self):
        self.fcount = round(self.fcount, 2)
        sfcount = format(self.fcount, ',')
        if self.fcount < 0:
            sfcount = sfcount.split('-')[1]
            return '-' + '$' + sfcount
        else:
            return '$' + sfcount

a = MoneyFmt(12345.6789)
print(a)

