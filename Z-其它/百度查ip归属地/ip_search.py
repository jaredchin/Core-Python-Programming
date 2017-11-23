import sys
import urllib.request
import json
'''
python3 调用百度IP归属地查询接口显示中文结果
'''
# url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=118.190.33.130&resource_id=6006&t=1511175501478&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery1102017679529467173427_1511175237779&_=1511175237794"

def get_ip_location(ip):
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=%s&resource_id=6006&t=1511175501478&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery1102017679529467173427_1511175237779&_=1511175237794' % ip
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Referer': r'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=monline_3_dg&wd=ip%E5%BD%92%E5%B1%9E%E5%9C%B0%E6%9F%A5%E8%AF%A2&rsv_pq=e10001cd00005b21&rsv_t=63cethNIR70qxJst2vrJZanOv5I2Xjq6nyFZnmQAfqo5aDnKwgbjSy0M3GNN07cNUXj7&rqlang=cn&rsv_enter=1&rsv_sug3=8&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&prefixsug=ipguishu&rsp=0&inputT=2637&rsv_sug4=2638',
        'Cookie': r'BAEID=7F2B0FC1585E2FE692DEE86E0195E2CD; BAIDUID=9CD8F78B214C5637921A427D37B7C314:FG=1; BIDUPSID=F9BCC32D14B548CB33A32CE3D385FF46; PSTM=1499406827; MCITY=-158%3A; __cfduid=d20822907badd05b722f0cc947831a0e01508829693; H_PS_PSSID=1430_21082; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; PSINO=2; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; BDRCVFR[Fc9oatPmwxn]=G01CoNuskzfuh-zuyuEXAPCpy49QhP8',
        'Connection': 'keep-alive',
        'Pragma': 'no - cache',
        'Cache - Control': 'no - cache'
    }
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    content = resp.read()
    return content

if __name__ == '__main__':
    content = get_ip_location('180.150.177.238').decode('gbk')
    content_json = content.split('[')[1].split(']')[0]
    content_dict = json.loads(content_json)
    print('%(origip)s的归属地为: %(location)s' %content_dict)

