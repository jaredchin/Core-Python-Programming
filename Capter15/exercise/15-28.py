import re

phone1 = '800-555-1212'
phone2 = '555-1212'

m = re.match('(\d{3}-){1,2}\d{4}', phone1)
print(m.group())

m = re.match('(\d{3}-){1,2}\d{4}', phone2)
print(m.group())