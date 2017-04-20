# encoding=UTF-8

'''
def log(func):
     # * 无名字的参数
     # ** 有名字的参数
    def wrapper(*args, **kwargs):
        print 'before calling ', func.__name__
        print 'args:', args, 'kwargs:', kwargs
        func(*args, **kwargs)
        print 'end calling ', func.__name__
    return wrapper

@log
def hello():
    print 'hello world'

@log
def hello2(name, age):
    print 'hello2', name, age

if __name__ == '__main__':
    hello()     # = log(hello())
    hello2('张山', 13)
    hello2(name='李思思', age=56)
'''

def log(level, *args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            '''
            * 用来传递任意个无名字参数，这些参数会一个Tuple的形式访问。
            **用来处理传递任意个有名字的参数，这些参数用dict来访问
            '''
            print level, 'before calling ', func.__name__
            print level, 'args:', args, 'kvargs:', kvargs
            func(*args, **kvargs)
            print level, 'after calling ', func.__name__
            print ''
        return wrapper
    return inner

@log(level='INFO')
def hello(name, msg):
    print 'hello', name, msg

if __name__ == '__main__':
    hello(name='nowcoder', msg='i miss you')