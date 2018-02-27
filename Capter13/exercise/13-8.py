class Stack(object):
    def __init__(self, alist):
        self.alist = alist

    def push(self, param):
        self.alist.append(param)
        return param

    def pop(self):
        if len(self.alist) > 0:
            result = self.alist[len(self.alist) - 1]
            self.alist = self.alist[:len(self.alist)-1]
            return result
        else:
            print('No item to pop')

    def isempty(self):
        if len(self.alist):
            return 0
        else:
            return 1

    def peek(self):
        return self.alist[len(self.alist) - 1]



alist = [1, 2, 3, 4, 5, 6]
stak = Stack(alist)
stak.push('qin')
print(stak.alist)
stak.pop()
print(stak.alist)
print(stak.isempty())
print(stak.peek())
stak.pop()
stak.pop()
print(stak.alist)
