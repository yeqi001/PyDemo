# 已知一个字符串为 “hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
def demo1():
    """
    将字符串分割为列表
    split('分隔符'，'分割次数，默认最大')
    """
    a = "hello_world_yoyo"
    b = a.split('_')
    print(b)


# 有个列表 [“hello”, “world”, “yoyo”]如何把把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”
def demo2():
    """
    Example1: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    Example2:
    strip() 方法用于截掉字符串首尾的空格或指定字符
    lstrip() 方法用于截掉字符串左边的空格或指定字符
    rstrip() 方法用于截掉字符串右边的空格或指定字符
    """
    a = ["hello", "world", "yoyo"]
    # b = '_'.join(a)
    # print(b)
    b = ''
    for i in a:
        b = b + "_" + i
    print(b.strip("_"))


# 把字符串 s 中的每个空格替换成”%20”
# 输入：s = “We are happy.”
# 输出：”We%20are%20happy.”
def demo3():
    """
    replace
    """
    s = "We are happy."
    # i = ''
    # for j in s:
    #     if j == " ":
    #         j = "%20"
    #     i = i + j
    i = s.replace(" ", "%20")
    print(i)


# 打印99乘法表
def demo4():
    """
    print() 方法默认end='\n'
    \t ：表示空4个字符，类似于文档中的缩进功能，相当于按一个Tab键。
    \n ：表示换行，相当于按一个 回车键
    \n\t : 表示换行的同时空4个字符
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            # print(str(i)+"*"+str(j)+"="+str(i*j),end='\t')
            # print('%d*%d=%d' % (i, j, i * j), end="\t")
            print('{}*{}={}'.format(i, j, i * j), end="\t")
        print(" ")


# 找出单词 “welcome” 在 字符串”Hello, welcome to my world.” 中出现的位置，找不到返回-1
# 从下标0开始索引
def demo5():
    """
     find() 方法检测字符串中是否包含子字符串 str,如果指定 beg（开始） 和 end（结束） 范围，
     则检查是否包含在指定范围内，如果包含子字符串 返回开始的索引值，否则返回-1。
    """
    a = "Hello, welcome to my world."
    b = "welcome"
    if b in a:
        print(a.find(b))
    else:
        print("-1")


# 统计字符串“Hello, welcome to my world.” 中字母w出现的次数
# 统计单词 my 出现的次数
def demo6():
    """
    count() 方法用于统计字符串里某个字符或子字符串出现的次数
    """
    i = 0
    a = "Hello, welcome to my world."
    for j in a:
        if "o" in j:
            i = i + 1
    print(i, a.count("my"))


# 输入一个字符串str, 输出第m个只出现过n次的字符，如在字符串 gbgkkdehh 中,
# 找出第2个只出现1 次的字符，输出结果：d
def demo7(a, b, c):
    """
    :param a:字符串
    :param b:第几次出现的
    :param c:出现次数
    :return:
    """
    i = 0
    for j in a:
        if a.count(j) == c:
            i += 1
            if i == b:
                print(j)


if __name__ == '__main__':
    demo7("gbgkkdehh", 2, 1)
