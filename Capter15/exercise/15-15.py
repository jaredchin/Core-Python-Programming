from re import match
data = input('Card NO: ')

ft1 = '[0-9]{15,16}'
ft2 = '[0-9]{4}-[0-9]{6}-[0-9]{5}'
ft3 = '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}'
m1 = match(ft1, data)
m2 = match(ft2, data)
m3 = match(ft3, data)

if m1 is not None:
    print(m1.group())
elif m2 is not None:
    print(m2.group())
elif m3 is not None:
    print(m3.group())