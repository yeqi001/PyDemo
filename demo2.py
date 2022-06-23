# -*- coding: utf-8 -*-
def a(b):
    i = 0
    while True:
        if b==0 or b==1:
            return 1
        yield i
        i,b=b-1,b-i
f = a(3)
#while True:
    print(next(f),None)
# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()