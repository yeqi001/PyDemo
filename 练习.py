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


# 已知 a的值为”hello”，b的值为”world”，如何交换a和b的值？
# 得到a的值为”world”，b的值为”hello”
def demo22():
    a = "hello"
    b = "world"
    c = b
    b = a
    a = c
    print(a, b)


# 如何判断一个数组是对称数组：
# 要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
# 用Python代码判断，是对称数组打印True，不是打印False,如：
# x = [1, “a”, 0, “2”, 0, “a”, 1]
def demo23():
    x = [1, "a", 0, "2", 0, "a", 1]
    j = 0
    # for i in range(len(x)//2):
    #     if x[i]==x[-(i+1)]:
    #         j+=1
    # if j ==len(x)//2:
    #     print("True")
    # else:
    #     print("False")
    if x == x[::-1]:
        print("True")
    else:
        print("False")


# 如果有一个列表a=[1,3,5,7,11]
# 问题：1如何让它反转成[11,7,5,3,1]
# 2.取到奇数位值的数字，如[1,5,11]
def demo24():
    a = [1, 3, 5, 7, 11]
    print(a[::-1])
    print(a[::2])


# 问题：对列表a 中的数字从小到大排序
# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
def demo25():
    """
    sorted() 函数对所有可迭代的对象进行排序操作，操作之后原对象依然存在
    sorted(iterable, key=None, reverse=False)
    iterable -- 可迭代对象。
    cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认)

    sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    list.sort(cmp=None, key=None, reverse=False)
    :return:
    """
    a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
    # for i in range(len(a)):
    #     for j in range(len(a)-1):
    #         if a[j]>a[j+1]:
    #             a[j],a[j+1]=a[j+1],a[j]
    # print(a)
    print(sorted(a, reverse=True))


# 取出列表中最大的三个值
# L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
def demo26():
    """
    [start:stop:step] 字符串、列表、元组(tuple)都符合“序列”这一特征然后进行切片,表示为[开始索引:结束索引(不包含该索引的值):步长]
    :return:
    """
    L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
    print(sorted(L1)[-1:-4:-1])


# a = [1, -6, 2, -5, 9, 4, 20, -3] 按列表中的数字绝对值从小到大排序
def demo27():
    """
    abs() 函数返回数字的绝对值。
    :return:
    """
    a = [1, -6, 2, -5, 9, 4, 20, -3]
    for i in range(len(a)):
        a[i] = abs(a[i])
    print(sorted(a))


# b = [“hello”, “helloworld”, “he”, “hao”, “good”]
# 按list里面单词长度倒叙
def demo28():
    b = ["hello", "helloworld", "he", "hao", "good"]
    print(sorted(b, key=len))


# 将列表中的重复值取出(仅保留第一个)，要求保留原始列表顺序
# 如a=[3, 2, 1, 4, 2, 6, 1] 输出[3, 2, 1, 4, 6]
def demo29():
    a = [3, 2, 1, 4, 2, 6, 1]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(b)


# a = [1, 3, 5, 7]
# b = [‘a’, ‘b’, ‘c’, ‘d’]
# 如何得到[1, 3, 5, 7, ‘a’, ‘b’, ‘c’, ‘d’]
def demo30():
    a = [1, 3, 5, 7]
    b = ["a", "b", "c", "d"]
    print(a + b)


# 列表a = [1,2,3,4,5], 计算列表成员的平方数，得到[1,4,9,16,25]
def demo31():
    a = [1, 2, 3, 4, 5]
    b = []
    for i in a:
        i = i ** 2
        b.append(i)
    print(b)


# 使用列表推导式，将列表中a = [1, 3, -3, 4, -2, 8, -7, 6]
# 找出大于0的数，重新生成一个新的列表
def demo32():
    a = [1, 3, -3, 4, -2, 8, -7, 6]
    b = []
    for i in a:
        if i > 0:
            b.append(i)
    print(b)
    print([i for i in a if i > 0])


# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
def demo33():
    a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
    b = c = 0
    for i in a:
        if i > 0:
            b += 1
        elif i < 0:
            c += 1
    print("正数：", b, "负数：", c)


# a = [“张三”,”张四”,”张五”,”王二”] 如何删除姓张的
def demo34():
    a = ["张三", "张四", "张五", "王二"]
    # 循环从len(a)-1开始到下标为0时结束，步长-1即倒着循环
    # 当删掉一个元素后，len(a)-1就会减1，此时len(a)-1还是最后一个元素的下标
    for i in range(len(a) - 1, -1, -1):
        if a[i][0] == "张":
            a.remove(a[i])
    print(a)


# 有个列表a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] 使用filter 函数过滤出大于0的数
def test_35(a):
    return a > 0


def demo35():
    """
    filter(function, iterable) 函数用于过滤序列，过滤掉不符合条件的元素，序列的每个元素作为参数传递给函数进行判断，
    然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
    function:判断函数
    iterable:可迭代对象
    :return:符合条件元素组成的新列表的内存地址
    """
    a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
    b = list(filter(test_35, a))
    print(b)


# 列表b = [“张三”, “张四”, “张五”, “王二”] 过滤掉姓张的姓名
def test_36(a):
    return a[0] != "张"


def demo36():
    b = ["张三", "张四", "张五", "王二"]
    c = list(filter(test_36, b))
    print(c)


# 过滤掉列表中不及格的学生
# a = [
# {“name”: “张三”, “score”: 66},
# {“name”: “李四”, “score”: 88},
# {“name”: “王五”, “score”: 90},
# {“name”: “陈六”, “score”: 56},
# ]
def test_37(a):
    return a["score"] >= 60


def demo37():
    b = [{"name": "张三", "score": 66},
         {"name": "李四", "score": 88},
         {"name": "王五", "score": 90},
         {"name": "陈六", "score": 56}]
    c = list(filter(test_37, b))
    print(c)


# 有个列表 a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
# 找出列表中最大的数，出现的位置，下标从0开始
def demo38():
    a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
    for i in range(len(a)):
        if a[i] == max(a):
            print(i)


# a = ['my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
# 'need', 'skills', 'more', 'my', 'ability', 'are',
# 'so', 'poor']
# 找出列表中出现次数最多的元素
def demo39():
    a = ['my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
         'need', 'skills', 'more', 'my', 'ability', 'are',
         'so', 'poor']
    b = 0
    for i in a:
        if a.count(i) > b:
            b = a.count(i)
    for i in a:
        if a.count(i) == b:
            print(i)
            break


# 给定一个整数数组A及它的大小n，同时给定要查找的元素val，
# 请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。
# 若该元素出现多次请返回第一个找到的位置
# 如 A1=[1, “aa”, 2, “bb”, “val”, 33]
# 或 A2 = [1, “aa”, 2, “bb”]
def demo40():
    A1 = [1, 'aa', 2, 'bb', 'val', 33]
    if A1.count('val') == 0:
        print("-1")
    for i in range(len(A1)):
        if A1[i] == 'val':
            print(i)
            break


# 给定一个整数数组nums 和一个目标值target ，请你在该数组中找出和为目标值的那两个整数，并返回他
# 们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 示例:
# 给定nums=[2，7，11，15]，target=9
# 因为nums[0] + nums[1] =2+7 = 9,所以返回[0， 1]
def demo41():
    nums = [2, 7, 11, 15]
    target = 18
    k = {}
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            k.update({nums[i] + nums[j]: {i, j}})
    for a in k.keys():
        if a == target:
            print(k[a])


# a = [[1,2],[3,4],[5,6]] 如何一句代码得到 [1, 2, 3, 4, 5, 6]
def demo42():
    a = [[1, 2], [3, 4], [5, 6]]
    b = []
    for i in a:
        for j in i:
            b.append(j)
    print(b)


# 二维数组取值(矩阵),有 a = [[“A”, 1], [“B”, 2]] ，如何取出 2
def demo43():
    a = [["A", 1], ["B", 2]]
    print(a[1][1])


# a = [“a”, “b”, “c”]
# b = [1, 2, 3]
# 如何得到 {‘a’: 1, ‘b’: 2, ‘c’: 3}
def demo44():
    a = ["a", "b", "c"]
    b = [1, 2, 3]
    c = {}
    for i in range(len(a)):
        c.update({a[i]: b[i]})
    print(c)


# 如下列表
# people = [{“name”:”yoyo”, “age”: 20},{“name”:”admin”, “age”: 28},{“name”:”zhangsan”, “age”: 25}],按年龄age从小到大排序
def demo45():
    people = [{"name": "张三", "score": 66},
              {"name": "李四", "score": 88},
              {"name": "王五", "score": 90},
              {"name": "陈六", "score": 56}]
    print(sorted(people, key=lambda a: a["score"]))


# 现有 nums=[2, 5, 7] ，如何在该数据最后插入一个数字 9 ，如何在2后面插入数字0
def demo46():
    """
    insert("索引位置","对象") 函数用于将指定对象插入列表的指定位置。
    :return:
    """
    nums = [2, 5, 7]
    nums.append(9)
    nums.insert(1, 0)
    print(nums)


# 有个列表a = [1, 2, 3, 4, 5, 6, 7, 8, 9]如何打乱列表a的顺序,每次得到一个无序列表
import random


def demo47():
    """
    random.shuffle(x) 将序列 x 随机打乱位置。
    :return:
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(a)
    print(a)


# 输出1-100除3余1 的数，结果为tuple
def demo48():
    """
    列表是可变对象，而元组是不可变对象
    :return:
    """
    a = []
    for i in range(1, 101):
        if i % 3 == 1:
            a.append(i)
    print(tuple(a))


# 将("a", "b", "c") 和(1, 2, 3)两个tuple转成(1, 2, 3)为key, ("a", "b", "c")为value的字典
def demo49():
    """
    zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
    """
    a = ("a", "b", "c")
    b = (1, 2, 3)
    c = list(zip(a, b))
    d = {}
    for i in c:
        d.update({i[1]: i[0]})
    print(d)


# 将字典里的值是数值型的转换为字符串，如a = {‘aa’: 11, ‘bb’: 222},得到{‘aa’: ‘11’, ‘bb’: ‘222’}
def demo50():
    """
    items() 方法以列表返回视图对象，是一个可遍历的key/value对,返回的是列表
    :return:
    """
    a = {"aa": 11, "bb": 222}
    for i in a.items():
        a.update({i[0]: str(i[1])})
    print(a)


# map函数有个列表a = [1, 2, 3, 4] 计算列表中每个数除以2 取出余数 得到 [1,0,1,0]
def demo51():
    a = [1, 2, 3, 4]
    print(list(map(lambda a: a % 2, a)))


# map函数对列表a=[1,3,5],b=[2,4,6]相乘得到[2,12,30]
def demo52():
    a = [1, 3, 5]
    b = [2, 4, 6]
    print(list(map(lambda a, b: a * b, a, b)))


# 两个字典合并a={“A”:1,”B”:2},b={“C”:3,”D”:4}
def demo53():
    a = {"A": 1, "B": 2}
    b = {"C": 3, "D": 4}
    a.update(b)
    print(a)


# m1={‘a’:1,’b’:2,’c’:1} # 将同样的value的key集合在list里，输出{1:[‘a’,’c’],2:[‘b’]}
def demo54():
    a = {"a": 1, "b": 2, "c": 1}
    b = {}
    for i, j in a.items():
        if j not in b:
            b[j] = [i]
        else:
            b[j].append(i)
    print(b)


# d={“name”:”zs”,”age”:18,”city”:”深圳”,”tel”:”1362626627”} 字典根据键从小到大排序
def demo55():
    d = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
    a = sorted(d, key=lambda b: b[0])  # a为列表
    b = {}
    for i in a:
        b[i] = d[i]
    print(b)


# a = [2, 3, 8, 4, 9, 5, 6],b = [2, 5, 6, 10, 17, 11]
# 1.找出a和b中都包含了的元素
# 2.a或b中包含的所有元素
# 3.a中包含而集合b中不包含的元素
import copy


def demo56():
    """
    a = [2, [3 , 8], 6]
    赋值:   拷贝的列表随原列表变化而变化；
    b = a
    浅拷贝: 当外层元素变化时，拷贝的列表不会随原列表变化而变化；内层元素变化时，浅拷贝才会变化；
    b = a[:]   b = a.copy()  b = list(a)
    深拷贝: 无论原列表怎么变化，深拷贝都不会改变。
    import copy
    b = copy.deepcopy(a)
    :return:
    """
    a = [2, 3, 8, 4, 9, 5, 6]
    b = [2, 5, 6, 10, 17, 11]
    c = []
    d = copy.deepcopy(b)
    e = []
    for i in a:
        if i in b:
            c.append(i)
        if i not in d:
            d.append(i)
        if i not in b:
            e.append(i)
    print(c, sorted(d), e)


# 函数计算10！
def demo57(a):
    """
    递归：自身不断调用自己
    :return:
    """
    if a == 1 or a == 0:
        return 1
    else:
        return a * demo57(a - 1)


# 有1、2、3、4数字能组成多少互不相同无重复数的三位数?,分别打印这些三位数的组合
def demo58():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                print(i * 100 + j * 10 + k)


# a = [11, 2, 33, 1, 5, 88, 3]
# 冒泡排序：
# 依次比较两个相邻的元素，如果顺序（如从小到大、首字母从A到Z）
# 错误就把他们交换过来
def demo59():
    a = [11, 2, 33, 1, 5, 88, 3]
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


# 有一个数据list of dict如下
# a = [
# {“yoyo1”: “123456”},
# {“yoyo2”: “123456”},
# {“yoyo3”: “123456”},
# ]
# 写入到本地一个txt文件，内容格式如下：
# yoyo1,123456
# yoyo2,123456
# yoyo3,123456
def demo60():
    a = [{"name1": "张三"},
         {"name2": "李四"},
         {"name3": "王五"},
         {"name4": "陈六"}]
    with open('../PyDemo/test.txt', 'w', encoding='utf-8') as f:
        for i in a:
            for i, j in i.items():
                f.write("{},{}\n".format(i, j))


if __name__ == '__main__':
    demo60()
