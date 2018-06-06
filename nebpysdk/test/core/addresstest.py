import base64
from nebpysdk.src.core.Address import Address

class addresstest:

    def __init__(self):
        # base 16 decode
        self.__pub = bytearray(base64.b16decode("04be110ae3154924b93881cba7ea9cfcb6d4866d2becac5ccb79bab5d7e22309796ed60effbe6990320e7d8a0cc19e6e8b235aa17fe467c4c6ae7f469dcbf65609",True))
        self.__addr = "n1TjT3XYnHSSAkESFvGXeoN9bdjY8o6tyCm"

    def string(self):
        print(len(self.__pub))
        addr = Address.new_address_from_pub_key(self.__pub)

        print("addr:", addr.string(), len(addr.string()))
        print(Address.parse_from_string(self.__addr).string())


if __name__ == '__main__':
    atest = addresstest()
    atest.string()