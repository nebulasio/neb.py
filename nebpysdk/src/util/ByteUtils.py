# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 下午9:21
# @Author  : GuoXiaoMin
# @File    : ByteUtils.py
# @Software: PyCharm


class ByteUtils:


    @classmethod #
    def bytes2integer(cls, arr):
        res = 0
        for i in range(len(arr)):
            res = (res << 8) + arr[i]
        print(res)
        return res

    @classmethod
    def integer2bytes(cls, num):
        res = bytearray(16)
        for i in range(16)[::-1]:
            res[i] = num % 256
            num = (num >> 8)
        return bytes(res)

    @classmethod
    def long2bytes(cls, num):
        res = bytearray(8)
        for i in range(8)[::-1]:
            res[i] = num % 256
            num = (num >> 8)
        return bytes(res)

    @classmethod
    def int2bytes(cls, num):
        res = bytearray(4)
        for i in range(4)[::-1]:
            res[i] = num % 256
            num = (num >> 8)
        return bytes(res)