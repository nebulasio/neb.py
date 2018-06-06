import base64
from nebpysdk.src.crypto.keystore.secp256k1.ECsignature import ECsignature
from nebpysdk.src.crypto.keystore.secp256k1.ECPrivateKey import ECPrivateKey

class ECSignaturetest:


    def __init__(self):
        self.__signature = ECsignature()
        self.__privateKey=bytearray(base64.b16decode("e07c7b293b2907474d7a9d431eea0138c2734b2865804dc2ebb6e8f9a40ac0e0", True))
        self.__signData=bytearray(base64.b16decode("ff0d7b40123af5813b6add3de99369cbf029a464f5b3b7bb2e1523d0862e1812", True))
        self.__signeddata=bytearray(base64.b16decode("d5f47ac3c2883adfc46bc252de7550465469ab1d958adc0249653e0cb0eaca1e2aaf3e951b3585864fbd85834b34966e12acf43e31a390e045bbddaf97d199e901", True))

    def sign(self):
        priv = ECPrivateKey(self.__privateKey)
        self.__signature.initSign(priv)
        sign = self.__signature.sign(self.__signData)
        print(sign)
        print(sign==self.__signeddata)

    def recover_pub(self):
        priv = ECPrivateKey(self.__privateKey)
        pub = self.__signature.recover_public(self.__signData, self.__signeddata)
        print(priv.public_key().encode())
        print(len(priv.public_key().encode()))
        print(pub.encode())

    def verify(self):
        priv = ECPrivateKey(self.__privateKey)
        self.__signature.init_verify(priv.public_key())
        result = self.__signature.verify(self.__signData, self.__signeddata)
        print(result)

if __name__ == "__main__":
    ec = ECSignaturetest()
    ec.sign()
    ec.recover_pub()
    ec.verify()