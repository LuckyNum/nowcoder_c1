#-*- encoding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class':'content'}):
        print div.text.strip(), '\n-----------'

def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', '123')
    strb = '  \n\rhello 123\r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(' ')
    print 9, strc.find('hello')

def demo_opration():
    print 1, 1+2, 5/2, 5*2, 5-2
    print 2, True, not True
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3
    print 5, 5|3, 5&3, 5^3
    x = 2
    y = 3.3
    print x, y, type(x), type(y)

def demo_buildinfunction():
    print 1, min(5, 3), max(2,1)
    print 2, len('xxxxxxxxxx'), len([1,2,3])
    print 3, abs(-2) # fabs,Math.fabs
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x + 3')
    print 7, chr(97), ord('a')

def demo_controlflow():
    score = 65
    if score > 99:
        print 1,'A'
    elif score >60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score <100:
        print score
        score += 10

    score = 65
    # for(int i = 0: i<10: ++i)
    # continue, break, pass
    for i in range(0, 10, 2):
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break

def demo_list():
    lista = [1, 2, 3] #vector<int> Araylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in lista
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort(reverse=True)
    print 11, listb
    listb.sort(reverse=False)
    print 12, listb
    print 13, listb * 2
    print 14, [0] * 14 #memset(src, 0 ,len)
    tuplea = (1, 2, 3)
    listaa = [1, 2, 3]
    listaa.append(4)
    print 15, listaa

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def demo_dict():
    dicta = {1:1, 2:2, 3:3}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value:', key, value
    dictb = {'+': add, '-': sub}
    print 4, dictb['+'](1, 2)
    print 5, dictb.get('-')(1, 2)
    dictb['*'] = 'x'
    print 6, dictb
    dicta.pop(3)
    print 7, dicta

def demo_set():
    seta = set([1, 2, 3])
    setb = set((2, 3, 4))
    # print 1, seta
    # seta.add(4)
    print 2, seta
    print 3, seta.intersection(setb), seta & setb
    print 4, seta | setb, seta.union(setb)
    print 5, seta - setb
    seta.add('x')
    print 6, seta
    print 7, seta.__len__()

if __name__ == '__main__':
    # print 'hello world'
    # comment
    # demo_string()
    # demo_opration()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    demo_set()