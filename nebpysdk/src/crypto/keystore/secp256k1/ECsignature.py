# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : ECsignature.py
# @Software: PyCharm
from nebpysdk.src.crypto.keystore.Algorithm import Algorithm
from nebpysdk.src.crypto.keystore.secp256k1.ECPublicKey import ECPublicKey
from nebpysdk.src.crypto.keystore.secp256k1.ECPrivateKey import ECPrivateKey
from nebpysdk.src.crypto.keystore.secp256k1.Secp256k1 import Secp256k1


class ECsignature:

    def __init__(self):
        pass

    def algorithm(self):
        return Algorithm.SECP256K1.get_type

    def init_sign(self, key: ECPrivateKey):
        self.__private_key = key

    def sign(self, data):
        return Secp256k1.sign(data, self.__private_key.get_key())

    def recover_public(self, data, signature):
        pub = Secp256k1.RecoverPubBytesFromSignature(data, signature)
        self.__pub_key = ECPublicKey(pub)
        return self.__pub_key

    def init_verify(self, pub_key):
        self.__pub_key = pub_key

    def verify(self, data, signature):
        return self.__pub_key.verify(data, signature)
