from datetime import date

class TimeFmt(object):
    def __init__(self, Time=date.today().timetuple()):
        self.time = Time
        self.prompt = """
        1 MDY
        2 MDYY
        3 DMY
        4 DMYY
        5 MODYY
        Input your choice:"""

    def update(self, Time=date.today().timetuple()):
        self.time = Time

    def display(self):
        yy = str(self.time[0])[-2:]
        yyyy = str(self.time[0])
        mm = str(self.time[1])
        dd = str(self.time[2])
        while True:
            timefmt = input(self.prompt).strip().lower()
            if timefmt == '1':
                print('%s/%s/%s' % (mm, dd, yy))
            elif timefmt == '2':
                print('%s/%s/%s' % (mm, dd, yyyy))
            elif timefmt == '3':
                print('%s/%s/%s' % (dd, mm, yy))
            elif timefmt == '4':
                print('%s/%s/%s' % (dd, mm, yyyy))
            elif timefmt == '5':
                print('%s %s, %s' % (mm, dd, yyyy))
            else:
                print(date.ctime(date.today()))

tmfmt = TimeFmt()
print(tmfmt.display())
