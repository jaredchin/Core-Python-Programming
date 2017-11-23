import random
import string

ip1 = '142.4.106.'    #65-69
ip2 = '107.149.61.'     #65-125
ip3 = '108.186.69.'     #65-125
ip4 = '108.186.8.'      #1-61
ip5 = '107.148.136.'    #45-125



def log(code):
    with open('iplist.txt', 'a', encoding='utf-8') as f:
        # 通过 file 参数可以把输出写入到文件 f 中
        # 需要注意的是 **kwargs 必须是最后一个参数
        print(code, file=f)


for i in range(45, 126):
    ip = ip5 + str(i)
    log(ip)

