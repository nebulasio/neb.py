# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Address.py
# @Software: PyCharm
import hashlib
import enum
from nebpysdk.src.util.Base58 import Base58
from nebpysdk.src.proto.generated.corepb import transaction_pb2

class Address:

    __PaddingByte = bytearray(b'\x19')
    __NebulasFaith = 'n'

    # AddressPaddingLength the length of headpadding in byte
    __AddressPaddingLength = 1

    # AddressTypeLength the length of address type in byte
    __AddressTypeLength = 1

    # AddressTypeIndex the index of address type bytes
    __AddressTypeIndex = 1

    # AddressDataLength the length of data of address in byte
    __AddressDataLength = 20

    # AddressChecksumLength the checksum of address in byte
    __AddressChecksumLength = 4

    # AddressLength the length of address in byte
    __AddressLength = __AddressPaddingLength + __AddressTypeLength + __AddressDataLength + __AddressChecksumLength

    # PublicKeyDataLength length of public key
    __PublicKeyDataLength = 65

    # AddressBase58Length length of base58(Address.address)
    __AddressBase58Length = 35

    class AddressType(enum.Enum):

        ACCOUNT = (bytearray('\x57'.encode("utf-8")))
        CONTRACT = (bytearray('\x58'.encode("utf-8")))

        def __init__(self, _type):
            self.__type = _type

        @property
        def get_type(self):
            return self.__type

    def __init__(self, address):
        self.__address = bytearray(address)

    def bytes(self):
        return self.__address

    def string(self):
        return Base58.encode(self.__address)

    def type(self):
        address_type = self.__address[self.__AddressTypeIndex]
        if Address.AddressType.ACCOUNT == address_type:
            return Address.AddressType.ACCOUNT
        elif Address.AddressType.CONTRACT == address_type:
            return Address.AddressType.CONTRACT
        else:
            raise Exception("unsupport address type")

    @classmethod
    def new_address(cls, _type, *args):
        if len(args) == 0:
            raise Exception("invalid argument(s)")
        if Address.AddressType.ACCOUNT != _type and Address.AddressType.CONTRACT != _type:
            raise Exception("invalid address type")

        addr_bytes = bytearray(cls.__AddressLength)
        addr_bytes[0] = cls.__PaddingByte[0]
        addr_bytes[cls.__AddressTypeIndex] = _type.get_type[0]

        sha3_256_value = hashlib.sha3_256()
        sha3_256_value.update(bytearray(args[0]))
        cls.check_sum(args[0])
        ripemd160_value = hashlib.new('ripemd160', sha3_256_value.digest())
        ripemd_160_value = ripemd160_value.digest()

        addr_bytes[cls.__AddressTypeIndex + 1: cls.__AddressTypeIndex + 1+cls.__AddressDataLength] = ripemd_160_value[:]
        check_data = bytearray(addr_bytes[0:cls.__AddressLength-cls.__AddressChecksumLength])
        checksum = cls.check_sum(bytearray(check_data))
        addr_bytes[cls.__AddressLength - cls.__AddressChecksumLength:] = checksum[:]

        return Address(addr_bytes)

    @classmethod
    def check_sum(cls, data):
        sha3_256_value = hashlib.sha3_256()
        sha3_256_value.update(bytearray(data))
        sha3_256value = bytearray(sha3_256_value.digest())
        return sha3_256value[0:cls.__AddressChecksumLength]

    @classmethod
    def new_address_from_pub_key(cls, pub):
        if len(pub) != cls.__PublicKeyDataLength:
            raise Exception("invalid pubKey for address")
        return cls.new_address(cls.AddressType.ACCOUNT, pub)

    @classmethod
    def new_contract_address(cls, from_addr, nonce):
        if len(from_addr) == 0 or len(nonce) == 0:
            raise Exception("invalid from or nonce")
        return cls.new_address(cls.AddressType.CONTRACT, from_addr, nonce)

    @classmethod
    def parse_from_string(cls, addr):
        if len(addr) != cls.__AddressBase58Length or addr[0] != cls.__NebulasFaith:
            raise Exception("invalid address string format")
        addr_bytes = bytearray(Base58.decode(addr))
        return cls.parse_from_bytes(addr_bytes)

    @classmethod
    def parse_from_bytes(cls, byte):
        if len(byte) != cls.__AddressLength or byte[0] != cls.__PaddingByte[0]:
            raise Exception("invalid address bytes")
        checksum = byte[cls.__AddressLength - cls.__AddressChecksumLength:]
        checkdata = byte[:cls.__AddressLength - cls.__AddressChecksumLength - 1]
        if cls.byte_equal(cls.check_sum(checkdata), checksum):
            raise Exception("invalid address check sum")
        return Address(byte)

    @classmethod
    def byte_equal(cls, a, b):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

    def is_valid_address(self, address: str):
        self.parse_from_string(address)

    def isValidAccountAddress(self, address: str):
        self.parse_from_string(address)

    def isValidContractAddress(self, address: str):
        self.parse_from_string(address)