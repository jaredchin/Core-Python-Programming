class MoneyFmt(object):
    def __init__(self, value=0.0):
        self.value = round(float(value), 2)

    def update(self, value=None):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        val = '$' + str(self.value)
        return val

    def __nonzero__(self):
        return int(self.value)




