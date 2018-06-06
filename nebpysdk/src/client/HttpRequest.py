# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : HttpRequest.py
# @Software: PyCharm
import requests
import json


class HttpRequest:

    _timeout = 10 # 30s

    class MyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, bytes):
                return str(obj, encoding='utf-8');
            return json.JSONEncoder.default(self, obj)

    @staticmethod
    def set_timeout(timeout=1000):
        HttpRequest._timeout = timeout

    @staticmethod
    def request(method, url_api, payload):
        header = {'Content-type': 'application/json', 'Accept': 'application/json'}
        payload = json.dumps(payload)
        if method == "post":
            context = requests.post(url_api, data=payload, headers=header, timeout=HttpRequest._timeout)
            return context
        elif method == "get":
            context = requests.get(url_api, params=payload, timeout=HttpRequest._timeout)
            return context
