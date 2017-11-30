adict = {}

for i in range(4):
    name = input('Input %d name: ' % i)
    number = input('Input %d number: ' % i)
    adict[name] = int(number)

print(adict)