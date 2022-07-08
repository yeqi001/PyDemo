import time
import os

# 格式化当前时间戳
filename = '{}.txt'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
filepath = '../PyDemo/1/'
# 判断路径是否存在，否则创建路径
if not os.path.exists(filepath):
    os.mkdir(filepath)
open(filepath + filename, 'w+')
