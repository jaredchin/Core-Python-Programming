import urllib
from urllib import request
from base64 import encodestring

LOGIN = 'wesc'
PASSWD = 'you'
URL = 'http://loclahost'


def handler_version(url):
    from urllib import parse
    hdlr = request.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = request.build_opener(hdlr)
    request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = request.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
    req.add_header('Authorization', 'Basic %s' % b64str)
    return req

for funcType in ('handler', 'request'):
    print('*** Using %s:' % funcType.upper())
    url = eval('%s_version' % funcType)(URL)
    f = request.urlopen(url)
    print(f.readline())
    f.close()