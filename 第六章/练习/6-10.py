str1 = list(input('Input a string: '))
str2 = ''

for i in str1:
    if i.isalpha():
        if i.islower():
            i = i.upper()
        else:
            i = i.lower()
    str2 = str2 + i

print(str2)