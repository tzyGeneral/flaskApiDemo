import base64
import json
from Crypto.Cipher import AES  # pip3 install pyCryptodome


class AESCipher:
    """AES加解密工具"""

    def __init__(self, key: bytes, iv: bytes):
        self.key = key
        self.iv = iv  # 16位字符，用来填充缺失内容，可固定值也可随机字符串，具体选择看需求。

    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        text_length = len(text.encode('utf-8'))
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def encrypt(self, raw: str):
        """加密"""
        raw = self.__pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw.encode('utf-8')))

    def decrypt(self, enc):
        """解密"""
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))


def m2dExcludeFields(obj, *args):
    """mongo转dict  排除特定字段"""
    model_dict = obj.to_mongo().to_dict()
    model_dict.pop('_id')
    if args:
        list(map(model_dict.pop, list(args)))
    return model_dict


def m2dLimitFields(obj, *args):
    """mongo转dict  返回特定字段"""

    def _m2dLimitFields(obj, *args):
        if not obj:
            return ''
        model_dict = obj.to_mongo().to_dict()
        if args:
            fields = list(set(model_dict.keys()) - (set(model_dict.keys()) & set(args)))
            list(map(model_dict.pop, fields))
        return model_dict

    resultList = []
    for m in obj:
        d = _m2dLimitFields(m, *args)
        resultList.append(d)
    return resultList


def dictLimitFields(d, *args):
    """限制字典的键并返回"""
    if args:
        fields = list(set(d.keys()) - (set(d.keys()) & set(args)))
        list(map(d.pop, fields))
    return d


if __name__ == '__main__':
    aesTool = AESCipher(key=b"1234567890123456", iv=b"1234567890123456")
    en = aesTool.encrypt("helloworld")

    de = aesTool.decrypt("CUVt7dQ2rgEuQ2TuNKDBeQ==")
    print(de)