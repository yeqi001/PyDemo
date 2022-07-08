# import redis
#
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# #r.set('name', 'runoob')  # 设置 name 对应的值
# print(r['name'])
import requests
import re
from stu_redis import RedisHandler

def login():
        url = 'http://172.16.20.45:80/dev-api/api/sign'
        data = {
                "action":"signin",
                'username':'admin',
                'password':'admin'
        }
        headers ={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Content-Type': 'application/json;charset=UTF-8',
                'Accept': 'application/json, text/plain, */*',
        }
        res = requests.post(url,json=data,headers=headers)
        print(res.status_code)
        print(res.cookies)
        print(res.json)
        # 把返回的cookie转换为字典
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        print(cookie)
        RedisHandler().set('cookies',cookie)
        #e_token= re.search('{"code": 200, "msg": "(.*?)"}',res.text).group(1)
        #token = RedisHandler().get('token')
        #print(e_token)
def user():
        url = 'http://172.16.20.45/dev-api/api/user '
        data = {
                "action":"listUser",
                "pageNum":1,
                "pageSize":5
        }
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Content-Type': 'application/json;charset=UTF-8',
                'Accept': 'application/json, text/plain, */*',
        }
        token = RedisHandler().get('token')
        res = requests.post(url, headers=headers, cookies=token)
        print(res.text)

if __name__ == '__main__':
        login()
        #user()