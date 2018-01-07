import os
files = filter(lambda x: x and x[0] != '.', os.listdir())

print(list(files))