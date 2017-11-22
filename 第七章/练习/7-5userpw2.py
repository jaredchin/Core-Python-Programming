db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another:'
            continue
        else:
            break
    pwd = input('passwd:')
    db[name] = pwd


def olduser():
    name = input('login:')
    pwd = input('password:')
    passwd = db.get(name)
    if passwd == pwd:
        print('welcome back, %s' % name)
    else:
        print('login incorrect')


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    Enter choice:"""

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            if choice not in 'neq':
                print('Invalid option, try again')
            else:
                chosen = True

        if choice == 'q': done = True
        if choice == 'n': newuser()
        if choice == 'e': olduser()

if __name__ == '__main__':
    showmenu()