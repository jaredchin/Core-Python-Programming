m = input('Please input a module name: ')
module = __import__(m)
ml = dir(module)
print(ml)

for i in ml:
    print('name: ', i)
    print('type: ', type(getattr(module, i)))
    print('value: ', getattr(module, i))
    print('')