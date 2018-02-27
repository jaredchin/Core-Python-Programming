

class User(object):
    carts = []
    print(carts)
    def buy(self, item):
        return Cart(item)


class Item(object):
    def __init__(self, item):
        self.item = item


class Cart(object):
    def __init__(self, item):
        self.items = []
        self.items.append(item)
        print(self.items)


banana = Item('banana')
apple = Item('apple')
orange = Item('orange')

mike = User()
mike.buy(banana.item)
mike.buy(apple.item)
mike.buy(orange.item)
mike.carts = Cart(banana.item)

print(mike.carts)

