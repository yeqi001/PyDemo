import redis


# redis处理器
class RedisHandler:

    def __init__(self):
        self.re = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """
        缓存中写入 str（单个）
        :param name: 缓存名称
        :param value: 缓存值
        :param ex: 过期时间（秒）
        :param px: 过期时间（毫秒）
        :param nx: 如果设置为True，则只有name不存在时，当前set操作才执行（新增）
        :param xx: 如果设置为True，则只有name存在时，当前set操作才执行(修改）
        :return:
        """
        self.re.set(name, value)

    def get(self, name):
        """
        读取缓存
        :param name:
        :return:
        """
        return self.re.get(name)

    def get_keys(self):
        # redis_client.hmset('d', d)
        # print(redis_client.hgetall('d'))
        pass

    def key_exit(self, key):
        """
        判断redis中的key是否存在
        :param key:
        :return:
        """
        return self.re.exists(key)
