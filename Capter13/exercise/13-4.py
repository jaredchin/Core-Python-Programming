import time, getpass, hashlib, shelve


class UserDatabase(object):
    def __init__(self, dbfile):
        self.db = shelve.open(dbfile)

    def __del__(self):
        self.db.close()

    def receive(self, prompt=None, flag=True):
        try:
            if flag:
                receiver = input(prompt).strip().lower()
            else:
                receiver = getpass.getpass()
        except(KeyboardInterrupt, EOFError):
            receiver = 'System Quit!'
        return receiver

    def signup(self):
        while True:
            user = self.receive('Signup:')
            if user in self.db:
                print('Username taken, try another!')
                continue
            elif not user.isalnum() or ' ' in user:
                print('Invalid username!')
                continue
            else:
                break
        psw = self.receive(flag=False)

        timeNow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.db[user] = hashlib.md5(psw.encode()).hexdigest(), timeNow
        print('>You have already signup, return to login page.>>>')

    def login(self):
        while True:
            user = self.receive('Login:')
            psw = self.receive(flag=False)
            if (user in self.db and self.db.get(user)[0] == hashlib.md5(psw.encode()).hexdigest()):
                break
            else:
                print('Password or username is not right, try again')
                continue
        diffTime = float(time.time() - time.mktime(time.strptime(self.db[user][1], '%Y-%m-%d %H:%M:%S'))) / 3600

        if diffTime <= 4:
            print('Your already logged in at: ', self.db[user][1])
        timeNow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.db[user] = hashlib.md5(psw.encode()).hexdigest(), timeNow
        print('>***Welcome, %s!***' % user)

    def admin(self):
        choice = input('del a user or show all users: ').strip()[0].lower()
        if choice == 'd':
            user = self.receive('Username: ')
            if user in self.db:
                del self.db[user]
                print('Remove %s ... Done!' % user)
            else:
                print('Username %s is not valid!' % user)
        elif choice == 's':
            for user in self.db:
                print(user)
        else:
            print('Invalid input!')

    def updatepsw(self):
        user = self.receive('Username: ')
        if user in self.db:
            psw = self.receive(flag=False)
            self.db[user] = psw
        else:
            print('Username error!')


def start():
    prompt = """
    (S)ignup
    (L)ogin
    (A)dmin
    (Q)uit
    >Enter your choice: """
    done = False

    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            if choice not in 'slaq':
                print('>Invalid option, try again!')
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 's':
            user_database.signup()
        if choice == 'a':
            user_database.admin()
        if choice == 'l':
            user_database.login()

if __name__ == '__main__':
    user_database = UserDatabase('userpw2.shelve')
    start()
