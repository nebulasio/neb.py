# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Api.py
# @Software: PyCharm
from nebpysdk.src.client.HttpRequest import HttpRequest
import requests
import json

class Api:

    def __init__(self, host="https://testnet.nebulas.io", api_version="v1"):
        self._host = host
        self._api_version = api_version
        self._path = "/user"

    def set_request(self, host="https://testnet.nebulas.io", api_version="v1"):
        self._host = host
        self._api_version = api_version

    def getNebState(self):
        return self.send_request("get", "/nebstate", {})

    def latestIrreversibleBlock(self):
        return self.send_request("get", "/lib", {})

    def getAccountState(self, addr: str, height: int =0):
        param = {
            'address': addr,
            'height': height
        }
        return self.send_request("post", "/accountstate", param)

    def call(self, from_addr: str, to_addr: str, value: str, nonce: int, gasprice: str, gaslimit: str, contract=None):
        data = {
            "from": from_addr,
            "to": to_addr,
            "value": value,
            "nonce": nonce,
            "gasPrice": gasprice,
            "gasLimit": gaslimit,
            "contract": contract
        }
        return self.send_request("post", "/call", data)

    def sendRawTransaction(self, b_data):
        #b_data = bytes(b_data.encoding())
        if isinstance(b_data, bytes):
            b_data = str(b_data)
        data = {
            "data": b_data
        }
        return self.send_request("post", "/rawtransaction", data)

    def getBlockByHash(self, hash, isfull=False):
        data = {
            "hash": hash,
            "full_fill_transaction": isfull
        }
        return self.send_request("post", "/getBlockByHash", data)

    def getBlockByHeight(self, height):
        param = {
            "height": height
        }
        return self.send_request("post", "/getBlockByHeight", param)

    def getTransactionReceipt(self, hash):
        param = {
            "hash": hash
        }
        return self.send_request("post", "/getTransactionReceipt", param)

    def getTransactionByContract(self, address):
        param = {
            "address": address
        }
        return self.send_request("post", "/getTransactionByContract", param)

    #on_download_progress is the callback function for the subscribed events
    def subscribe(self, topics, on_download_progress):
        param = {
            "topics": topics
        }
        header = {'Content-type': 'application/json'}
        url = self._host + '/' + self._api_version + self._path + '/subscribe'
        data = json.dumps(param)
        response = requests.post(url, stream=True, data=data, headers=header)
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                on_download_progress(chunk.decode("utf8"))  #'byte' object to 'str' object
        return

    def gasPrice(self):
        param = {}
        return self.send_request("get", "/getGasPrice", param)

    def estimateGas(self, from_addr, to_addr, value, nonce, gasprice, gaslimit, contract=None, binary =None):
        param = {
            "from": from_addr,
            "to": to_addr,
            "value": value,
            "nonce": nonce,
            "gasPrice": gasprice,
            "gasLimit": gaslimit,
            "contract": contract,
            "binary": binary
        }
        return self.send_request("post", "/estimateGas", param)

    def getEventsByHash(self, hash):
        param = {
            "hash": hash
        }
        return self.send_request("post", "/getEventsByHash", param)

    def getDynasty(self, height):
        param = {
            "height": height
        }
        return self.send_request("post", "/dynasty", param)

    def create_url(self, api):
        return self._host + '/' + self._api_version + api

    def send_request(self, method, api, param):
        action = self._path + api
        url_api = self.create_url(action)
        return HttpRequest.request(method, url_api, param)
