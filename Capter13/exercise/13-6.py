import math
class StraightLine(object):
    def __init__(self, x1=0,y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return '(%s, %s), (%s, %s)' % (self.x1, self.y1, self.x2, self.y2)

    __repr__ = __str__

    def length(self):
        self.leng1 = self.y2 - self.y1
        self.leng2 = self.x2 - self.x1
        leng = math.sqrt(self.leng1 ** 2 + self.leng2 ** 2)
        return round(leng, 2)

    def slope(self):
        k = self.leng1 / self.leng2
        return round(k, 2)

line = StraightLine(1, 2, 3, 4)
print(line)
print(line.length())
print(line.slope())
