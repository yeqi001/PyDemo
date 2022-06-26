# 装饰器练习
from functools import wraps


def decorator_name(f):
    i = 0
    @wraps(f)
    def decorator(*args,**kwargs):
        global i
        i +=1
        print(f.__name__ + " was called")
        f(*args,**kwargs)
        print("第%d次"%i + f.__name__ + " was called")
    return decorator

@decorator_name
def demo57(a):
    sum = 0
    for i in range(1, a + 1):
        sum += i * 10 + 3
    print(sum)

if __name__ == '__main__':
     for i in range(3):
        demo57(10)