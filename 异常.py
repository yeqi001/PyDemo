# -*- coding: utf-8 -*-
name = input("姓名：")
age = input("年龄：")
try:
    for i in name:
        if i >= "0" and i <= "9":
            raise Exception("姓名不能有数字")
    if age <= "0":
        raise Exception("年龄不能小于0")
# except Exception as f:
#     print(f)

except Exception as f:
    print(f)
else:
    print("%s%s岁了" % (name, age))
finally:
    print("不管程序如何最后都会执行！！！")