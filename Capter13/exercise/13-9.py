class Queue(object):
    def __init__(self, alist):
        self.alist = alist

    def enqueue(self, param):
        self.alist.append(param)
        return param

    def dequeue(self):
        aparam = self.alist[0]
        self.alist = self.alist[1:]
        return aparam


alist = [5, 4, 8, 7]
queue = Queue(alist)
print(queue.enqueue(10))
print(queue.alist)
print(queue.dequeue())
print(queue.alist)
