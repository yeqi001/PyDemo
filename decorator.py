# -*- coding: utf-8 -*-
from functools import wraps
import time

def log(logfile="11.txt"):
    def logging(fun):
        @wraps(fun)
        def decorator(*args,**kwargs):
            with open('../PyDemo/'+logfile, 'a',encoding='utf-8') as f:
                starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                f.write('{} was called in {} \n'.format(fun.__name__,starttime))
                result = fun(*args,**kwargs)
                f.write(str(result)+'\n')
                endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                f.write('{} was end in {} \n'.format(fun.__name__,endtime))
                return result
        return decorator
    return logging

@log()
def test(a):
    return a+a


print(test(2))
