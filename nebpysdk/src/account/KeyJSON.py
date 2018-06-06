# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : KeyJson.py
# @Software: PyCharm
from nebpysdk.src.crypto.cipher.CryptoJSON import CryptoJSON
import uuid


class KeyJson:

    def __init__(self, address, crypto):
        self.address = address
        self.crypto = crypto
        self.id = str(uuid.uuid1())
        self.version = CryptoJSON.VERSION

    def get_address(self):
        return self.address

    def set_address(self, address: str):
        self.address = address

    def get_crypto(self):
        return self.crypto

    def set_crypto(self, crypto: CryptoJSON):
        self.crypto = crypto

    def get_id(self):
        return self.id

    def set_id(self, id: str):
        self.id = id

    def get_version(self):
        return self.version

    def set_version(self, version: int):
        self.version = version
