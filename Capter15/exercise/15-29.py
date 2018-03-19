import re

phone1 = '800-555-1212'
phone2 = '555-1212'
phone3 = '(800) 555-1212'

m = re.match('.*\d{3}-\d{4}', phone3)
print(m.group())
