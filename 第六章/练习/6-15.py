import time
inputtime1 = input("Please input a time(DD/MM/YY): ")
inputtime2 = input("Please input another time(DD/MM/YY): ")

atime1 = time.mktime(time.strptime(inputtime1, "%d/%m/%Y"))
atime2 = time.mktime(time.strptime(inputtime2, "%d/%m/%Y"))


if atime1 >= atime2:
    days = (atime1-atime2) / 86400
    print("相差%d天" % days)
else:
    days = (atime2 - atime1) / 86400
    print("相差%d天" % days)