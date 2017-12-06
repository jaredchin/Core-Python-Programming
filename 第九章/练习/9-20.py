import gzip

f_in = open(r'test.txt', 'rb')
f_out = gzip.open(r'test.txt.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

f = gzip.open(r'test.txt.gz', 'rb')
f_out = open(r'test1.txt', 'wb')
content = f.read()
f_out.write(content)
f.close()
f_out.close()

