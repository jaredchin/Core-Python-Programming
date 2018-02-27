import time, json

db = {300059: [u'东方财富', 'Wes Jul 13 15:15:12 2016', 22,43, 1000]}
db_json = json.dumps(db, ensure_ascii=False)

class Bond(object):
    def add(self, code, arr):
        db_json[code] = arr

    def dele(self, code):
        if code in db_json:
            print('%s sold out.' % code)
            del db_json[code]
        else:
            print('No such stock code.')