# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : ECPublicKey.py
# @Software: PyCharm
from nebpysdk.src.crypto.keystore.Algorithm import Algorithm
from nebpysdk.src.crypto.keystore.secp256k1.Secp256k1 import Secp256k1


class ECPublicKey:

    def __init__(self, pub):
        self.__pubKey = pub

    def algorithm(self):
        return Algorithm.SECP256K1

    def encode(self):
        return self.__pubKey

    def decode(self, data):
        self.__pubKey = data

    def clear(self):
        self.__pubKey = bytearray(len(self.__pubKey))

    def verify(self, data, signature):
        return Secp256k1.Verify(data, signature, self.__pubKey)
