# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : ECPrivateKey.py
# @Software: PyCharm
from nebpysdk.src.crypto.keystore.Algorithm import Algorithm
from nebpysdk.src.crypto.keystore.secp256k1.ECPublicKey import ECPublicKey
from nebpysdk.src.crypto.keystore.secp256k1.Secp256k1 import Secp256k1
from eth_keys import keys


class ECPrivateKey:

    @classmethod
    def generate_key(cls):
        eckey = Secp256k1.GenerateECKey()
        return ECPrivateKey(eckey.to_bytes())

    def __init__(self, data: bytes) -> None:
        self.__seckey = keys.PrivateKey(data)

    def algorithm(self):
        return Algorithm.SECP256K1

    def get_key(self):
        return self.__seckey

    def encode(self) -> bytes:
        return self.__seckey.to_bytes()

    def decode(self, data: bytes):
        self.__seckey = data

    def clear(self) -> None:
        self.__seckey = bytearray(len(self.__seckey))

    def public_key(self) -> ECPublicKey:
        pub = Secp256k1.private_key_to_public_key(self.__seckey)
        pub = b'\x04'+pub.to_bytes()
        return ECPublicKey(pub)

    def sign(self, data):
        return Secp256k1.sign(data, self.__seckey)


