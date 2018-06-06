# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Neb.py
# @Software: PyCharm
from nebpysdk.src.client.Api import Api
from nebpysdk.src.client.Admin import Admin


class Neb:


    # todo host_const

    def __init__(self):
        self.api = Api()
        self.admin = Admin()

    def set_request(self):
        self.api.set_request()
        self.admin.set_request()

