import base64
from nebpysdk.src.crypto.cipher.Cipher import Cipher
from nebpysdk.src.crypto.keystore.Algorithm import Algorithm
import json
from nebpysdk.src.crypto.cipher.CryptoJSON import CryptoJSON

class ciphertest:

    _pass_phrase = "passphrase"
    private_key = base64.b16decode("e07c7b293b2907474d7a9d431eea0138c2734b2865804dc2ebb6e8f9a40ac0e0",True)
    crypto = "{\"cipher\":\"aes-128-ctr\",\"ciphertext\":\"bea1c02c9b290524e371da1d27f879ece0b85fe3975f69a7118bbbc9211dbc06\",\"cipherparams\":{\"iv\":\"4fdb9a9fc1c5dd8b6512dbedfdd08fd3\"},\"kdf\":\"scrypt\",\"kdfparams\":{\"dklen\":32,\"n\":4096,\"p\":1,\"r\":8,\"salt\":\"4d3ac8dcf01a25c097590f15f00b8999f3836e99a9957606f96b98de1f8ec838\"},\"mac\":\"6504d33980ee905fef4e04f083e23b1631606d59046cbbd3d4140f84276328d3\",\"machash\":\"sha3256\"}";


    def encrypt(self):
        cipher = Cipher(Algorithm.SCRYPT)
        crypto_json = cipher.encrypt(self.private_key, bytes(self._pass_phrase.encode("utf-8")))
        print(crypto_json.__dict__)
        key = cipher.decrypt(crypto_json, bytes(self._pass_phrase.encode("utf-8")))
        print(key)
        print("--------------------------------")

    def decrypt(self):
        cipher = Cipher(Algorithm.SCRYPT)
        crypto_json = json.loads(self.crypto)
        crypto = CryptoJSON()
        crypto.__dict__ = crypto_json
        cipherparams = CryptoJSON.CipherParams()
        cipherparams.__dict__ = crypto.cipherparams
        crypto.cipherparams= cipherparams

        scrypt = CryptoJSON.ScryptParams()
        scrypt.__dict__ = crypto.kdfparams
        crypto.kdfparams = scrypt
        print(crypto_json)
        print(crypto.__dict__)
        print(crypto.kdfparams.__dict__)
        print(crypto.cipherparams.__dict__)
        key = cipher.decrypt(crypto, bytes(self._pass_phrase.encode("utf-8")))
        print(key)
        for i in range(len(self.private_key)):
            print(self.private_key[i])
        print("======================")
        for i in range(len(key)):
            print(key[i])


if __name__ == "__main__":
    test = ciphertest()
    test.encrypt()
    test.decrypt()