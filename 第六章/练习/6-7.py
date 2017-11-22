#输入一个数字
num_str = input('Enter a number: ')

#将输入的数字转换为int类型
num_num = int(num_str)

#获取一个序列数字
fac_list = [x for x in range(1, num_num+1)]

#打印该序列
print("Before:", fac_list)

#赋初始值
i = 0

#循环
while i < len(fac_list):

    if num_num % fac_list[i] == 0:
        del fac_list[i]

    i = i +1


print("AFTER：", fac_list)