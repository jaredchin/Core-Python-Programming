
class Message(object):
    def __init__(self, fr, to, info):
        self.fr = fr
        self.to = to
        self.info = info

    def fr(self):
        return self.fr

    def to(self):
        return self.to

    def info(self):
        return self.info


class User(object):
    def __init__(self, username, sex):
        self.username = username
        self.sex = sex

    def __str__(self):
        return '%s, %s' % (self.username, self.sex)

    __repr__ == __str__

    def send(self, room, to, info):
        message = Message(self.username, to, info)
        return room.reciver(message)

    def quit_room(self, room):
        return room.quit(self.username)

    def create_room(self, roomname):
        return Room(roomname, self.username)


class Room(object):
    def __init__(self, roomname, creater):
        self.roomname = roomname
        self.users = []
        self.users.append(creater)

    def __str__(self):
        return '%s: created by %s, members: %s' % (self.roomname, self.users[0], ' '.join(self.users))

    __repr__ == __str__

    def invite(self, user):
        self.user = user
        self.users.append(user.username)
        print('%s has been ivited .' % user.username)

    def reciver(self, message):
        if message.fr in self.users:
            if message.to in self.users:
                print('%s@%s:%s' % (message.fr, message.to, message.info))
            elif message.to == 'all':
                print('%s@%s:%s' % (message.fr, message.to, message.info))
            else:
                print('%s is not in this room' % message.to)
        else:
            print('You are not in this room')

    def quit(self, username):
        try:
            self.users.remove(username)
            print('%s has quit.' % username)
        except(ValueError):
            print('You are not in this room')
