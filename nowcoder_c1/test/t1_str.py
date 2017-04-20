# -*- encoding:UTF-8 -*-

def func01():
    # 01.将一串字符串反向输出，如将"abcd"变成"dcba"
    str1 = "abcd"
    print 01, str1[::-1]

def func02():
    # 02.判断是否为回文——判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”。
    while(1):
        input_str = raw_input("请输入字符串：")
        if input_str == "quit":
            print "bye"
            break
        elif input_str == input_str[::-1]:
            print "此字符串是回文"
        else:
            print "此字符串不是回文"

def func03():
    # 统计一段英文语句的字母个数
    input_str = raw_input("请输入英文句子：")
    count = {}
    for i in input_str:
        count.setdefault(i, 0)  #如果字典中没有key为i的键，则添加这个键，并设置该键的值为0。如果已经有这个键了，则不更改该字典
        count[i] = count[i]+1
    print "字母个数：", count

def func04():
    # 统计一段英文语句中单词的个数
    input_str = raw_input("请输入英文句子：")
    strlist = input_str.split(" ")
    countWord = {}
    for i in strlist:
        countWord.setdefault(i,0)
        countWord[i] = countWord[i] + 1
    print "单词个数：", countWord

if __name__ == '__main__':
    # func01()
    # func02()
    # func03()
    func04()