option = """
Please input your choice:
(C)reate new file
(R)eplace old file"""

def cleanfile(filename):
    choice = input(option)
    if choice == 'c':
        dfile = input('Please input the new filename:')
        sf = open(filename, 'r')
        df = open(dfile, 'w')
        for eachLine in map(lambda line:line.strip(), sf):
            df.write(eachLine + '\n')
        sf.close()
        df.close()
    elif choice == 'r':
        sf = open(filename, 'r')
        sflines = sf.readlines()
        sf.close()
        df = open(filename, 'w')
        for eachLine in sflines:
            df.write(eachLine.strip() + '\n')
        df.close()


cleanfile('test.txt')