# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Scrypt.py
# @Software: PyCharm
from nebpysdk.src.crypto.cipher.CryptoJSON import CryptoJSON
import pyscrypt
#import Crypto.Cipher.AES
from Crypto.Cipher import AES
from nebpysdk.src.crypto.hash.Hash import Hash
import base64
from Crypto.Util import Counter
import binascii
import os


def int_of_string(iv):
    return int(binascii.hexlify(iv), 16)


class Scrypt:

    def encrypt(self, data: bytes, passphrase: bytes) -> CryptoJSON:

        # scrypt
        salt = os.urandom(CryptoJSON.ScryptDKLen)
        derived_key = pyscrypt.hash(passphrase,
                                    salt,
                                    CryptoJSON.StandardScryptN,
                                    CryptoJSON.StandardScryptR,
                                    CryptoJSON.StandardScryptP,
                                    CryptoJSON.ScryptDKLen)
        encrypt_key = derived_key[0:16]

        # AEC encrypt
        iv = os.urandom(16)
        ctr = Counter.new(128, initial_value=int_of_string(iv))
        aes = AES.new(encrypt_key, AES.MODE_CTR, counter=ctr)
        crypted_str = aes.encrypt(data)

        # sha3256
        mac_derived_key = derived_key[16: 32]
        mac = Hash.sha3256(mac_derived_key, crypted_str, iv, bytes(CryptoJSON.CIPHERNAME.encode("utf-8")))

        # generate crypto_json
        cipher_params = CryptoJSON.CipherParams()
        cipher_params.iv = base64.b16encode(iv).lower()
        scrypt_params = CryptoJSON.ScryptParams()
        scrypt_params.n = CryptoJSON.StandardScryptN
        scrypt_params.r = CryptoJSON.StandardScryptR
        scrypt_params.p = CryptoJSON.StandardScryptP
        scrypt_params.dklen = CryptoJSON.ScryptDKLen
        scrypt_params.salt = base64.b16encode(salt).lower()
        crypto_json = CryptoJSON()
        crypto_json.cipher = CryptoJSON.CIPHERNAME
        crypto_json.ciphertext = base64.b16encode(crypted_str).lower()
        crypto_json.cipherparams = cipher_params
        crypto_json.kdf = CryptoJSON.ScryptKDF
        crypto_json.kdfparams = scrypt_params
        crypto_json.mac = base64.b16encode(mac).lower()
        crypto_json.machash = CryptoJSON.MACHASH
        return crypto_json

    def decrypt(self, crypto_json: CryptoJSON, passphrase: bytes, version: int = 4) -> bytes: #todo v3 match

        # check kdf&cipher
        if CryptoJSON.CIPHERNAME != crypto_json.cipher.lower():
            raise Exception("invalid cipher")
        if CryptoJSON.ScryptKDF != crypto_json.kdf.lower():
            raise Exception("kdf not support")

        # scrypt
        mac = base64.b16decode(crypto_json.mac, True)
        iv = base64.b16decode(crypto_json.cipherparams.iv, True)
        cipher_text = base64.b16decode(crypto_json.ciphertext, True)
        salt = base64.b16decode(crypto_json.kdfparams.salt, True)
        dklen = crypto_json.kdfparams.dklen
        n = crypto_json.kdfparams.n
        r = crypto_json.kdfparams.r
        p = crypto_json.kdfparams.p
        derived_key = pyscrypt.hash(passphrase, salt, n, r, p, dklen)
        mac_derived_key = derived_key[16:32]

        # sha3256
        if version == 4:
            cal_mac = Hash.sha3256(mac_derived_key, cipher_text, iv, bytes(crypto_json.cipher.encode("utf-8")))
        elif version == 3:
            cal_mac = Hash.sha3256(mac_derived_key, cipher_text)
        if mac != cal_mac:
            raise Exception("could not decrypt key with given passphrase")
        encrypt_key = derived_key[0:16]
        ctr = Counter.new(128, initial_value=int_of_string(iv))
        aes = AES.new(encrypt_key, AES.MODE_CTR, counter=ctr)

        # AEC decrypt
        crypted = aes.decrypt(cipher_text)
        return crypted
