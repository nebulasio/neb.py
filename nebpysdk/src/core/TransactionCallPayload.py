# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : TransactionCallPayload.py
# @Software: PyCharm
from nebpysdk.src.core.TransactionPayload import TransactionPayload
import json
import re


class TransactionCallPayload(TransactionPayload):

    @classmethod
    def dict2_transaction_call_payload(cls, data):
        return TransactionCallPayload(data['_function'],data['args'])

    @classmethod
    def load_payload(cls, data):
        payload = json.loads(data, object_hook=cls.dict2_transaction_call_payload)
        return TransactionCallPayload(payload.get_function(), payload.get_args())

    def __init__(self, _function, args):
        self.Function = _function
        self.Args = args

    def check_args(self, _function, args):
        if re.match(r'^[a-zA-Z$][A-Za-z0-9_$]*$', _function):
            raise  Exception("invalid function of call payload")

        if args != None and args.length() > 0:
            str_json = json.loads(args)

    def get_function(self):
        return self.Function

    def set_function(self,_function):
        self.Function = _function

    def get_args(self):
        return self.Args

    def set_args(self, args):
        self.Args = args

    def to_bytes(self):
        return bytes(json.dumps(self.__dict__).encode())

    def gas_count(self):
        return 60

