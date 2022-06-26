# -*- coding: utf-8 -*-
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


if __name__ == '__main__':
    while True:
        a = int(input("请输入第一个数："))
        b = int(input("请输入第二个数："))
        c = input("请输入加减乘除：")
        cal = Calculator(a, b)
        if c == "加":
            print(cal.add())
            break
        elif c == "减":
            print(cal.subtract())
            break
        elif c == "乘":
            print(cal.multiply())
            break
        elif c == "除":
            print(cal.divide())
            break
        else:
            print("请输入加减乘除！！！")
            continue
