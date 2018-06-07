# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : TransactionBinaryPayload.py
# @Software: PyCharm
from nebpysdk.src.core.TransactionPayload import TransactionPayload


class TransactionBinaryPayload(TransactionPayload):

    @classmethod
    def load_payload(cls, data):
        return TransactionBinaryPayload(data)

    def __init__(self, data):

        if type(data) is str:
            data = bytes(data.encode())

        self.data = bytes(data)

    def to_bytes(self):
        return self.data

    def gas_count(self):
        return 0


