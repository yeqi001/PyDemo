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


if __name__ == '__main__':
    demo4()
