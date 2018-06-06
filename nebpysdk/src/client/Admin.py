# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Admin.py
# @Software: PyCharm
from nebpysdk.src.client.HttpRequest import HttpRequest


class Admin:

    def __init__(self, host="https://testnet.nebulas.io", api_version="v1"):
        self._host = host
        self._api_version = api_version
        self._path = "/admin"

    def set_request(self, host="https://testnet.nebulas.io", api_version="v1"):
        self._host = host
        self._api_version = api_version

    def nodeInfo(self):
        return self.send_request("get", "/nodeinfo", {})

    def account(self):
        return self.send_request("get", "/accounts", {})

    def newAccount(self, passphrase):
        param = {
            "passphrase": passphrase
        }
        return self.send_request("post", "/account/new", param)

    def unlockAccount(self, address, passphrase, duration = '30000000000'):
        param = {
            'address': address,
            "passphrase": passphrase,
            "duration": duration,
        }
        return self.send_request("post", "/account/unlock", param)

    def lockAccount(self, address):
        param = {
            'address': address
        }
        return self.send_request("post", "/account/lock", param)

    def sendTransaction(self, from_addr: str, to_addr: str, value: str, nonce: int, gasPrice: str, gasLimit: str, type: str, contract: dict, binary: str):
        param = {
            "from": from_addr,
            "to": to_addr,
            "value": value,
            "nonce": nonce,
            "gasPrice": gasPrice,
            "gasLimit": gasLimit,
        }
        return self.send_request("post", "/transaction", param)

    def signHash(self, address:str, hash: str, alg:int =1):
        param = {
            'address': address,
            'hash': hash,
            'alg': alg
        }
        return self.send_request("post", "/sign/hash", param)

    def signTransactionWithPassphrase(self, from_addr: str, to_addr: str,
                                      value: str, nonce: str,
                                      gasPrice: str, gasLimit: str,
                                      type: str, contract: str, binary: str,
                                      passphrase: str):
        tx = {
            "from": from_addr,
            "to": to_addr,
            "value": value,
            "nonce": nonce,
            "gasPrice": gasPrice,
            "gasLimit": gasLimit,
            'type': type,
            "contract": contract,
            "binary": binary
        }
        param = {
            "transaction": tx,
            "passphrase": passphrase
        }
        return self.send_request("post", "/transactionWithPassphrase", param)

    def startPprof(self, listen: str):
        param = {
            "listen": listen
        }
        return self.send_request("post", "/pprof", param)

    def getConfig(self):
        param = {}
        return self.send_request("get", "/getConfig", param)

    def create_url(self, api):
        return self._host + '/' + self._api_version + api

    def send_request(self, method, api, param):
        action = self._path + api
        url_api = self.create_url(action)
        return HttpRequest.request(method, url_api, param)