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
    replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
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


# 判断字符串a=”welcome to my world” 是否包含单词b=”world”,包含返回True，不包含返回 False
def demo8():
    a = "welcome to my world"
    b = "worla"
    # 判断b存在次数，非0为"True"
    if a.count(b):
        # if b in a:
        print("True")
    else:
        print("False")


# 输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
# 从 0 开始计数
# A = “hello”
# B = “hi how are you hello world, hello yoyo !”
def demo9():
    A = "hello"
    B = "hi how are you hello world, hello yoyo !"
    print(B.find(A))


# 输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A, 出-1从 0 开始计数
# A = “hello”
# B = “hi how are you hello world, hello yoyo !”
def demo10():
    A = "hello"
    B = "hi how are you hello world, hello yoyo !"
    i = -1
    while True:
        C = B.find(A, i + 1)
        if C == -1:
            print(i)
            break
        else:
            i = C


# 给定一个数a，判断一个数字是否为奇数或偶数 ,a1 = 13,a2 = 10
def demo11():
    """
    int() 函数用于将一个数字字符串或数字转换为整型。
    float() 函数用于将整数和字符串转换成浮点数。
    :return:
    """
    while True:
        # try:
        # a=int(input("1:"))
        a = int("123")
        # except ValueError:
        #    print("1")
        #    continue
        if a % 2 == 0:
            print("偶数")
            break
        else:
            print(type(a), "奇数")
            break


# 输入一个姓名，判断是否姓王,a = “王五”,b = “老王
def demo12():
    a = input("姓名：")
    if a[0] == "王":
        print("姓王")
    else:
        print("不姓王")


# 如何判断一个字符串是不是纯数字组成  a = “123456”  b = “yoyo123”
def demo13(a):
    try:
        float(a)
        print("是")
    except ValueError:
        print("不是")


# 将字符串 a = “This is string example….wow!” 全部转成大写
# 字符串 b = “Welcome To My World” 全部转成小写
def demo14():
    """
    upper() 方法将字符串中的小写字母转为大写字母
    lower() 方法转换字符串中所有大写字符为小写。
    :return:
    """
    a = "This is string example….wow!"
    b = "Welcome To My World"
    print(a.upper(), a.lower())


# 将字符串 a = “ welcome to my world “首尾空格去掉
def demo15():
    a = " welcome to my world "
    print(a.strip(" "))


# 打印菱形
def demo16():
    # a = int(input("菱形长度："))
    a = 9
    for i in range(int(a / 2) + 1):  # 先打印上面一半（包括最长的一行）
        for j in range(int(a / 2) - i):  # i=0的时候打印第一行
            print(end=" ")  # 每行遍历的时候通过end只打印“ ”不换行
        for k in range(2 * i + 1):  # i=0的时候先打印上面循环的空格，然后开始遍历每行的“*”
            print("*", end="")  # 每行遍历的时候通过end只打印“*”不换行
        print("")  # 每一行打印完之后进行换行操作
    for q in range(int(a / 2)):  # 打印下面的一半，其他原理同上
        for w in range(q + 1):
            print(end=" ")
        for e in range(a - 2 * (q + 1)):
            print("*", end="")
        print("")


# 题目 给一个不多于5位的正整数，要求：
# 一、求它是几位数，
# 二、逆序打印出各位数字。
# a = 12345
def demo17():
    """
    ‘/’：传统除法，输出为浮点数
    ‘//’：（地板除），结果取整数部分
    ‘%’：结果取余数部分
    :return:
    """
    a = 1512
    b = 0
    c = str(a)
    d = c[::-1]
    print(d)
    while a != 0:
        b += 1
        a = a // 10
    print(b)


# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# 那么问题来了，求1000以内的水仙花数（3位数）
def demo18():
    for a in range(100, 1000):
        b = str(a)
        c = list(b)
        if a == int(c[0]) ** 3 + int(c[1]) ** 3 + int(c[2]) ** 3:
            print(a)


# 求1+2+3…+100和
def demo19():
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)


# 计算求1-2+3-4+5-…-100的值
def demo20():
    a = b = 0
    for i in range(1, 101):
        if i % 2 != 0:
            a += i
        else:
            b -= i
    print(a + b)


# 计算公式 13 + 23 + 33 + 43 + …….+ n3
# 实现要求：
# 输入 : n = 5
# 输出 : 165
# 对应的公式 : 13 + 23 + 33 + 43 + 53 = 165
def demo21(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * 10 + 3
    print(sum)


if __name__ == '__main__':
    demo21(5)
