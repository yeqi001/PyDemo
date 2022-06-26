# -*- coding: utf-8 -*-
name = 5
def a():
    #global name
    name = 1
    print(name)

def b():
    name=9
    print(name)


sum= lambda a,b:a+b
sum(1,2)
print(sum(1,2))
max=(lambda a,b:a if a>b else b)(1,3)
print(max)