strip = input("Please input the ip adress: ")

if len(strip) != 12 or not strip.isdigit():
    exit('wrong ip adress')

listip = list(strip)


for i in range(1, 12):
    if i %3 == 0:
        listip[i] = '.' + listip[i]

ipaddress = ''.join(listip)
print(ipaddress)

listip_reverse = list(reversed(list(strip)))
for i in range(1, 12):
    if i %3 == 0:
        listip_reverse[i] = '.' + listip_reverse[i]

ipaddress_reverse = ''.join(listip_reverse)
print(ipaddress_reverse)


