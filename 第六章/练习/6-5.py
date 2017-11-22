##############b#############
# astring = input('请输入一个字符串a： ')
# bsting = input('请输入一个字符串b： ')
#
# if len(astring) != len(bsting):
#     print('no')
#     exit()
#
#
# for i, j in zip(astring, bsting):
#     if i is not j:
#         print('no')
#         exit()
# else:
#     print('yes')

##############c###############
# str1 = input('请输入一个字符串: ')
# if int(len(str1)%2) != 0:
#     print('no')
#     exit()
# elif str1[0:int(len(str1)/2)] == str1[int(len(str1)/2):int(len(str1))]:
#     print('yes')
#     exit(1)
# else:
#     print('not')

#############d#########################
str1 = input('请输入一个字符串: ')
str2 = str1
i = int(len(str1))
while i >= 1:
    str2 = str2 + str1[i-1]
    i -= 1

print(str2)
