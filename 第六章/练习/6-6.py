a = input('请输入一个字符串： ')

i = int(len(a))
j = 0
while j < i:
    if a[j] == ' ':
        j += 1
        continue
    elif a[j] != ' ':
        b = a[j:]
        break


l = int(len(b)) - 1

while l >= 0:
    if b[l] == ' ':
        l -= 1
        continue
    elif b[l] != ' ':
        c = b[:l]
        break

print(c)