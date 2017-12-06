import os

def createfile():
    filename = input('Please input the filename you want to create: ')
    i = 1
    lines = []
    while True:
        line = input('Please input the %d line: ' % i)
        if line == 'ENDLINE':
            break
        else:
            lines.append(line)
            i += 1
    f = open(filename, 'w')
    for j in lines:
        f.write(j + '\n')
    f.close()

def viewfile():
    filename = input('Which file you want to see: ')
    if os.path.isfile(filename):
        f = open(filename, 'r')
        for eachLine in f:
            print(eachLine, end='')
    else:
        print('Wrong filename')
        exit(0)


def editfile():
    filename = input('Which file you want to edit: ')
    linenum = int(input('Which line you want to edit: '))
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    lines[linenum-1] = input('Please input the content: ') + '\n'
    f = open(filename, 'w')
    for line in lines:
        f.write(line)
    f.close()

def showmenu():
    prompt = """
    (N)ew file
    (V)iew file content
    (E)dit file
    (Q)uit
    Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)

            if choice not in 'nveq':
                print('Invalid option, try again')
            else:
                chosen = True

        if choice == 'q': done = True
        if choice == 'n': createfile()
        if choice == 'v': viewfile()
        if choice == 'e': editfile()


if __name__ == '__main__':
    showmenu()