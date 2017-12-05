import os

def FilePathCheck(F):
    if os.path.isfile(F):
        return F
    path = os.getcwd()
    curdirF = os.path.join(path, F)
    if os.path.isfile(curdirF):
        return curdirF
    return

if __name__ == '__main__':
    F = input('Please input the file name:')
    file_path = FilePathCheck(F)
    if file_path:
        with open(file_path) as f:
            while True:
                try:
                    input('Press any key to continue...')
                    for i in range(25):
                        line = f.readline()
                        if line == '':
                            raise EOFError
                        print(line, end='')
                except(EOFError, KeyboardInterrupt):
                    break
    else:
        print('the file name is not valid!')