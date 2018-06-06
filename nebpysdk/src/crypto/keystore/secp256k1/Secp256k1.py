# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Secp256k1.py
# @Software: PyCharm
from eth_keys import KeyAPI
from eth_keys import keys
from eth_keys.backends.native import ecdsa
from eth_keys import KeyAPI
from eth_keys.backends import NativeECCBackend
import os


class Secp256k1:


    def __init__(self):
        pass


    @classmethod
    def GenerateECKey(cls):
        return keys.PrivateKey(os.urandom(32))

    @classmethod
    def Verify(cls, data, sign, pub):
        signature = keys.Signature(sign)
        return KeyAPI().ecdsa_verify(data, signature, pub)

    @classmethod
    def private_key_to_public_key(cls, data):
        return KeyAPI().private_key_to_public_key(data)

    @classmethod
    def key_api(cls):
        return KeyAPI(backend=NativeECCBackend())

    def private_key(key_api):
        return key_api.PrivateKey(os.urandom(32))

    @classmethod
    def sign(cls, data, key):
        return KeyAPI().ecdsa_sign(message_hash=data, private_key=key)

    @classmethod
    def RecoverPubBytesFromSignature(cls, data, sign):
        signature = keys.Signature(sign)
        return KeyAPI().ecdsa_recover(data, signature)