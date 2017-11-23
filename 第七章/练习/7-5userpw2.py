import hashlib

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
    db[name] = encodepass(pwd)


def olduser():
    name = input('login:')
    pwd = input('password:')
    passwd = db.get(name)
    if passwd == encodepass(pwd):
        print('welcome back, %s' % name)
    else:
        print('login incorrect')


def deluser():
    name = input('Del user: ')
    if name in db:
        del db[name]
        print('user %s has delete.' % name)
    else:
        print('user %s is not valid!' % name)


def viewuser():
    if db == {}:
        print('no user regist!')
    else:
        for key in db:
            print('user:%s passwd:%s' % (key, db[key]))


def encodepass(passwd):
    m = hashlib.md5()
    m.update(passwd.encode(encoding="utf-8"))
    return m.hexdigest()


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (D)elete user
    (V)eiw all user
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
            if choice not in 'neqdv':
                print('Invalid option, try again')
            else:
                chosen = True

        if choice == 'q': done = True
        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'd': deluser()
        if choice == 'v': viewuser()

if __name__ == '__main__':
    showmenu()

