class RoomRateCalc(object):
    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        daily = round(self.roomRate*(1 + self.roomTax + self.salesTax), 2)
        return float(days) * daily

sfo = RoomRateCalc(299)
print(sfo.calcTotal(1))
print(sfo.calcTotal(2))
print('-' * 22)
sea = RoomRateCalc(189, 0.086, 0.058)
print(sea.calcTotal())
print(sea.calcTotal(4))
print('-' * 22)
wasWkDay = RoomRateCalc(169, 0.045, 0.02)
wasWkEnd = RoomRateCalc(119, 0.045, 0.02)
print(wasWkDay.calcTotal(5) + wasWkEnd.calcTotal())


# python3 round()函数用作四舍五入时，会出现不准确的情况，避免用round函数做精确地四舍五入计算
print(round(1.5))
print(round(0.5))
print('-' * 40)
print(round(1.15, 1))
print(round(1.25, 1))
print(round(1.35, 1))
