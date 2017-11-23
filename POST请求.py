import urllib
import http.cookiejar
import json

import requests
def testrequests():
    url = "http://bbs.211600.com/mocuz/3.0/index.php"
    params = {
        'nameAccount': '4006233000',
        'uid': '9666403620',
        'cb': 'JSONP_CALLBACK_13_62'
    }
    #re = requests.post(url, params)
    re = requests.get("http://hb.crm2.qq.com", params)
    return re

if __name__ == '__main__':
    re = testrequests()
    print(re.text)
