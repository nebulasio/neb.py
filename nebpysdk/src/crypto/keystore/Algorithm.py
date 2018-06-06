# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Algorithm.py
# @Software: PyCharm
import enum


class Algorithm(enum.Enum):

    # SECP256K1 a type of signer
    SECP256K1 = 1

    # SCRYPT a type of encrypt
    SCRYPT = (1 << 4)

    def __init__(self, _type):
        self.__type = _type

    @property
    def get_type(self):
        return self.__type

    @classmethod
    def from_type(cls, type):
        if Algorithm.SECP256K1.get_type == type:
            return Algorithm.SECP256K1
        elif Algorithm.SCRYPT.get_type == type:
            return Algorithm.SCRYPT
        else:
            raise Exception("invalid algorithm")

