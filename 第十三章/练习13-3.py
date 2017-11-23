class MoneyFmt(object):
    def __init__(self, mcount=0.0, flag='-'):
        self.mcount = mcount
        self.flag = flag

    def dollarize(self):
        val = round(self.mcount, 2)
        strval = str(val)
        pos = strval.find('.')
        if strval.startswith('-'):
            while (pos-3)>1:
                strval = strval[:pos-3]+','+strval[pos-3:]
                pos -= 3
        else:
            while (pos-3)>0:
                strval = strval[:pos-3]+','+strval[pos-3:]
                pos -= 3
        if strval.startswith('-'):
            return self.flag + '$' + strval[1:]
        else:
            return '$' + strval

    def update(self, newvalue=None):
        if newvalue is not None:
            self.mcount = float(newvalue)

    def __nonzero__(self):
        if(self.mcount == 0):
            return False
        else:
            return True

    def __str__(self):
        return self.dollarize()

    def __repr__(self):
        return repr(self.mcount)

c = MoneyFmt(mcount=12312.1231)
c.__str__