import random
import string
# seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# sa = []
# for i in range(6):
#     sa.append(random.choice(seed))
# salt = ''.join(sa)


def log(code):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # 通过 file 参数可以把输出写入到文件 f 中
        # 需要注意的是 **kwargs 必须是最后一个参数
        print(code, file=f)
#
#
# for m in range(100):
#     seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     sa = []
#     for i in range(6):
#         sa.append(random.choice(seed))
#     salt = ''.join(sa)
#     log(salt)
#     salt = ''




seed = "输赢"
sa = []
for i in range(100):
    sa.append(random.choice(seed))
salt = ''.join(sa)
log(salt)
salt = ''


