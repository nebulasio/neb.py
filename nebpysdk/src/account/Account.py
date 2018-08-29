# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Account.py
# @Software: PyCharm
from nebpysdk.src.crypto.keystore.secp256k1.ECPrivateKey import ECPrivateKey
from nebpysdk.src.crypto.cipher.Cipher import Cipher
from nebpysdk.src.crypto.keystore.Algorithm import Algorithm
from nebpysdk.src.account.KeyJSON import KeyJson
import json
from nebpysdk.src.crypto.cipher.CryptoJSON import CryptoJSON
from nebpysdk.src.core.Address import Address
import base64


class Account:

    def __init__(self, private_key=None):
        if private_key is None:
            private_key = ECPrivateKey.generate_key()
        elif isinstance(private_key,str):
            private_key = ECPrivateKey(bytes.fromhex(private_key))
        elif isinstance(private_key,bytes):
            private_key = ECPrivateKey(private_key)
        self.__private_key = private_key
        self.__publickey = self.__private_key.public_key()
        self.__address = Address.new_address_from_pub_key(self.__publickey.encode())

    def set_privatekey(self, pri_key_str: str):
        pri_key_bytes = bytearray(base64.b16decode(pri_key_str, True))
        priv = ECPrivateKey(pri_key_bytes)
        return Account(priv)

    @classmethod
    def new_account(cls, private_key=None):
        # private_key = ECPrivateKey.generate_key()
        return Account(private_key)

    def to_key(self, password):

        # check password
        if type(password) is str:
            password = "passphrase".encode('UTF-8')
        elif type(password) is not bytes:
            raise Exception("password must be string or bytes")

        # encrypt
        cipher = Cipher(Algorithm.SCRYPT)
        crypto_json = cipher.encrypt(self.get_private_key(), password)

        # generate json
        key_json = KeyJson(self.get_address_str(), crypto_json)
        re = {
            "version": key_json.get_version(),
            "id": key_json.get_id(),
            "address": key_json.get_address(),
            "crypto": {
                "ciphertext": key_json.get_crypto().get_ciphertext(),
                "cipherparams": {
                    "iv": key_json.get_crypto().get_cipherparams().get_iv(),
                },
                "cipher": key_json.get_crypto().get_cipher(),
                "kdf": key_json.get_crypto().get_kdf(),
                "kdfparams": {
                    "dklen": key_json.get_crypto().get_kdfparams().get_dklen(),
                    "salt": key_json.get_crypto().get_kdfparams().get_salt(),
                    "n": key_json.get_crypto().get_kdfparams().get_n(),
                    "r": key_json.get_crypto().get_kdfparams().get_r(),
                    "p": key_json.get_crypto().get_kdfparams().get_p()
                },
                "mac": key_json.get_crypto().get_mac(),
                "machash": key_json.get_crypto().get_machash()
            },
        }
        return json.dumps(re)

    @classmethod
    def from_key(cls, key_data: str, password: bytes):

        # check password
        if type(password) is str:
            password = bytes(password.encode())

        if type(password) is not bytes:
            raise Exception("password must be bytes or str")

        # json to dict
        key_data_json = cls.__is_valid_json(key_data)

        # dict to object & check
        crypto = CryptoJSON()
        crypto.__dict__ = key_data_json['crypto']
        cipherparams = CryptoJSON.CipherParams()
        cipherparams.__dict__ = crypto.cipherparams
        crypto.set_cipherparams(cipherparams)
        scrypt = CryptoJSON.ScryptParams()
        scrypt.__dict__ = crypto.kdfparams
        crypto.set_kdfparams(scrypt)

        # to KeyJson
        # key_json = KeyJson(key_data_json['address'], crypto)

        # decrypt to pri_key
        cipher = Cipher(Algorithm.SCRYPT)
        pri_key_str = cipher.decrypt(crypto, password, key_data_json['version'])
        pri_key = ECPrivateKey(bytes(pri_key_str))

        # new Account
        account = Account(pri_key)
        return account

    @classmethod
    def __is_valid_json(cls, key_data):  # v3 test
        key_data_json = json.loads(key_data)
        if all(key not in key_data_json for key in ["version", "id", "address", "crypto"]):
            raise Exception("invalid json")
        if all(key not in key_data_json['crypto'] for key in ["ciphertext", "cipherparams", "mac", "machash", "cipher", "kdf", "kdfparams"]):
            raise Exception("invalid crypto json")
        if all(key not in key_data_json['crypto']['cipherparams'] for key in ["iv"]):
            raise Exception("invalid cipherparams json")
        if all(key not in key_data_json['crypto']['kdfparams'] for key in ["dklen", "salt", "n", "r", "p"]):
            raise Exception("invalid kdfparams json")
        return key_data_json

    def get_private_key(self) -> bytes:
        return self.__private_key.encode()

    def get_private_key_obj(self) -> ECPrivateKey:
        return self.__private_key

    def get_public_key(self) -> bytes:
        return self.__publickey.encode()

    def get_address_str(self) -> str:
        return self.__address.string()

    def get_address_obj(self) -> Address:
        return self.__address
