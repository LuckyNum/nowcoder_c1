# -*- encoding:UTF-8 -*-
import random
import re

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

def demo_exception():
    try:
        print 2/1
        # print 2/0
        raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print 'error:', e
    finally:
        print 'clean up'

def demo_random():
    # 1 - 100
    random.seed(1)

    print 1, int(random.random() * 100)
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 4)
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print 5, a

def demo_re():
    str = 'abc123def456gf45'
    p1 = re.compile('[\d]+')
    print 1, p1.findall(str)

if __name__ == '__main__':
    # user1 = User('zhangsan', 1)
    # print user1
    # admin1 = Admin('lisi', 2, "groupA")
    # print admin1
    # print creat_user('USER')
    # print creat_user('XXX')
    # demo_exception()
    # demo_random()
    demo_re()