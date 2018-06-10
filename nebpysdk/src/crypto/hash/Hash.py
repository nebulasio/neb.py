# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Hash.py
# @Software: PyCharm
import hashlib
# from Crypto.Hash import SHA3_256 as SHA3

class Hash:

    @classmethod
    def sha3256(cls, *args):
        sha3_256_value = hashlib.sha3_256()
        for i in range(len(args)):
            arg_byte = args[i]
            if type(arg_byte) is not bytes:
                arg_byte = bytes(arg_byte)
            sha3_256_value.update(arg_byte)
        return sha3_256_value.digest()


    @classmethod
    def ripemd160(cls, *args):
        pass
