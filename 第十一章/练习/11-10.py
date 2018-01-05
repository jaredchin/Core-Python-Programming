import os

files = filter(lambda x: x and x[0] != '.', os.listdir())
print(list(files))


#这里filter的作用是过滤掉了'.'开头的文件