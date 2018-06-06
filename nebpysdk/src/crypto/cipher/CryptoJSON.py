# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : CryptoJSON.py
# @Software: PyCharm
class CryptoJSON:

    # version
    VERSION = 4

    ScryptKDF = "scrypt"

    StandardScryptN = 1 << 12

    StandardScryptR = 8

    StandardScryptP = 1

    # ScryptDKLen get derived key length
    ScryptDKLen = 32

    # cipher the name of cipher
    CIPHERNAME = "aes-128-ctr"

    # mac calculate hash type
    MACHASH = "sha3256"

    class CipherParams:

        def __init__(self):
            pass

        def get_iv(self) -> str:
            return bytes.decode(self.iv)

        def set_iv(self, iv: str) -> None:
            self.iv = iv

    class ScryptParams:

        def __init__(self):
            pass

        def get_n(self) -> int:
            return self.n

        def set_n(self, n: int) -> None:
            self.n = n

        def get_r(self) -> int:
            return self.r

        def set_r(self, r: int) -> None:
            self.r = r

        def get_p(self) -> int:
            return self.p

        def set_p(self, p: int) -> None:
            self.p = p

        def get_dklen(self) -> int:
            return self.dklen

        def set_dklen(self, dklen: int) -> None:
            self.dklen =dklen

        def get_salt(self) -> int:
            return bytes.decode(self.salt)

        def set_salt(self, salt: str) -> None:
            self.salt = salt

    def get_cipher(self) -> str:
        return self.cipher

    def set_cipher(self, cipher: str) -> None:
        self.cipher = cipher

    def get_ciphertext(self) -> str:
        return bytes.decode(self.ciphertext)

    def set_ciphertext(self, ciphertext):
        self.ciphertext = ciphertext

    def get_cipherparams(self) -> CipherParams:
        return self.cipherparams

    def set_cipherparams(self, cipherparams: CipherParams) -> None:
        self.cipherparams = cipherparams

    def get_kdf(self) -> str:
        return self.kdf

    def set_kdf(self, kdf: str) -> None:
        self.kdf = kdf

    def get_kdfparams(self) -> ScryptParams:
        return self.kdfparams

    def set_kdfparams(self, kdfparams: ScryptParams):
        self.kdfparams = kdfparams

    def get_mac(self) -> str:
        return bytes.decode(self.mac)

    def set_mac(self, mac: str):
        self.mac = mac

    def get_machash(self) -> str:
        return self.machash

    def set_machash(self, machash:str) -> None:
        self.machash = machash