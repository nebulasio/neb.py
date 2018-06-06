# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Cipher.py
# @Software: PyCharm
from nebpysdk.src.crypto.keystore.Algorithm import Algorithm
from nebpysdk.src.crypto.cipher.Scrypt import Scrypt
from nebpysdk.src.crypto.cipher.CryptoJSON import CryptoJSON


class Cipher:

    def __init__(self, algorithm: Algorithm) -> None:
        if algorithm == Algorithm.SCRYPT:
            self._encrypt = Scrypt()
        else:
            raise Exception("unknown algorithm")

    def encrypt(self, data: bytes, passphrase: bytes) -> CryptoJSON:

        # check data
        if type(data) is not bytes:
            raise Exception("data must be bytes")

        # check passphrase
        if type(passphrase) is not bytes:
            raise Exception("passphrase must be bytes")

        return self._encrypt.encrypt(data, passphrase)

    def decrypt(self, data, passphrase: bytes, version: int = 4):

        # check passphrase
        if type(passphrase) is not bytes:
            raise Exception("passphrase must be bytes")

        if isinstance(data, CryptoJSON):
            return self._encrypt.decrypt(data, passphrase, version)
        else:
            raise Exception("invalid crypto")

