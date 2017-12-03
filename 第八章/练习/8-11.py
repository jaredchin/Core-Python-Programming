num = int(input('Enter total number of names: '))

wrongnum = 0
namelist = []

for i in range(0, num):
    name = input('Please enter name %d:' % i)
    while True:
        if ',' in name:
            namelist.append(name)
            break
        else:
            wrongnum += 1
            name = input('Your have done this %d time(s) already. Fixing input...' % wrongnum)
            continue

for j in sorted(namelist):
    print(j)
