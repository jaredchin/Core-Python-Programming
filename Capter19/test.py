import urllib
from urllib import request
from base64 import encodestring

LOGIN = 'wesc'
PASSWD = 'you'
URL = 'http://loclahost'


def handler_version(url):
    from urllib import parse as up
    hdlr = request.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', up(url)[1], LOGIN, PASSWD)
    opener = request.build_opener(hdlr)
    request.install_opener(opener)
    return url

def request_version(url):

