# -*- coding: utf-8 -*-
with open("../PyDemo/test.txt",'w+') as f:
    #f.read()
    #f.seek(0)
    #print(f.read())
    f.write("111122")
    f.seek(0)
    print(f.readline())