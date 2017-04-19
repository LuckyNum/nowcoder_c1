# -*- encoding = UTF-8 -*-

class User:
    type = 'USER'
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'i\'m ' + self.name + ' #' + str(self.uid)

class Admin(User):
    type = 'ADMIN'
    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'i\'m ' + self.name + ' #' + str(self.uid) + ' @' + self.group
class Guest(User):
    def __repr__(self):
        return 'i\'m guest:' + self.name + ' #' + str(self.uid)

def creat_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 1, 'g1')
    else:
        return Guest('gu1', 1)
        # raise ValueError('error')

if __name__ == '__main__':
    user1 = User('zhangsan', 1)
    print user1
    admin1 = Admin('lisi', 2, "groupA")
    print admin1
    print creat_user('USER')
    print creat_user('XXX')