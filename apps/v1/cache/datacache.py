from apps import memCache


class DataCache:
    """基础缓存类"""

    def __init__(self, timeout=60*60*3):
        self.cache = memCache.cache
        self.timeout = timeout

    def cleanKeyStr(self, key: str):
        """清理key的不规则写法"""
        key = str(key).replace(' ', '').strip()
        return key

    def get(self, key: str):
        """获取一个缓存"""
        key = self.cleanKeyStr(key)
        result = self.cache.get(key)
        return result

    def set(self, key: str, value):
        """设置一个缓存key-value"""
        key = self.cleanKeyStr(key)
        self.cache.set(key, value, self.timeout)

    def get_many(self, keyList: list):
        """获取多个缓存"""
        keyList = [self.cleanKeyStr(x) for x in keyList]
        result = self.cache.get_many(keyList)
        return result

    def set_many(self, mapping):
        """设置多个缓存值"""
        self.cache.set_many(mapping, self.timeout)