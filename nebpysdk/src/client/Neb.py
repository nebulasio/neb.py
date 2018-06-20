# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Neb.py
# @Software: PyCharm
from nebpysdk.src.client.Api import Api
from nebpysdk.src.client.Admin import Admin


class Neb:


    # todo host_const

    def __init__(self, provider=None, api_version="v1"):
        self.api = Api(provider, api_version)
        self.admin = Admin(provider, api_version)

    def set_request(self, provider):
        self.api.set_request(provider)
        self.admin.set_request(provider)

