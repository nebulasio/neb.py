# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Transaction.py
# @Software: PyCharm
import enum
import time
from nebpysdk.src.proto.generated.corepb import transaction_pb2
from nebpysdk.src.core.Address import Address
from nebpysdk.src.account.Account import Account
from nebpysdk.src.crypto.hash.Hash import Hash
from nebpysdk.src.crypto.keystore.secp256k1.ECsignature import ECsignature
from nebpysdk.src.crypto.keystore.Algorithm import Algorithm
from nebpysdk.src.util.ByteUtils import ByteUtils
import base64


class Transaction:

    # TransactionMaxGasPrice max gasPrice:1 * 10 ** 12
    __TransactionMaxGasPrice = 1000000000000

    # TransactionMaxGas max gas:50 * 10 ** 9
    __TransactionMaxGas = 50000000000

    # TransactionGasPrice default gasPrice : 10**6
    __TransactionGasPrice = 1000000

    # MinGasCountPerTransaction default gas for normal transaction
    __MinGasCountPerTransaction = 20000

    # GasCountPerByte per byte of data attached to a transaction gas cost
    __GasCountPerByte = 1

    # MaxDataPayLoadLength Max data length in transaction
    __MaxDataPayLoadLength = 1024 * 1024

    # MaxDataBinPayloadLength Max data length in binary transaction
    __MaxDataBinPayloadLength = 64

    class PayloadType(enum.Enum):

        BINARY = "binary"
        DEPLOY = "deploy"
        CALL = "call"

        def __init__(self, _type):
            self.__type = _type

        @property
        def get_type(self):
            return self.__type

    def __init__(self, chain_id, from_account, to_addr, value, nonce, payload_type, payload, gas_price, gas_limit):

        if type(chain_id) is not int:
            raise Exception("chain_id type must be int")
        if type(from_account) is not Account:
            raise Exception("from_account type must be Account")
        if type(to_addr) is not Address:
            raise Exception("to_addr type must be Address")
        if type(value) is not int:
            raise Exception("value type must by int")
        if type(nonce) is not int:
            raise Exception("nonce type must be int")
        if type(payload) is not bytes:
            raise Exception("payload type must be bytes")
        if type(gas_price) is not int:
            raise Exception("gas_price type must be int")
        if type(gas_limit) is not int:
            raise Exception("gas_limit type must be int")

        if gas_price > self.__TransactionMaxGasPrice or gas_price > self.__TransactionMaxGas:
            raise Exception("invalid gasPrice")

        if payload is not None and len(payload) > self.__MaxDataPayLoadLength:
            raise Exception("payload data length is out of max length")


        self.chain_id = chain_id
        self.__from_account = from_account
        self.from_addr = from_account.get_address_obj()

        self.to_addr = to_addr
        self.value = value
        self.nonce = nonce
        self.gas_price = gas_price
        self.gas_limit = gas_limit
        self.timestamp = int(round(time.time() * 1000))

        transaction = transaction_pb2.Transaction()
        setattr(transaction.data, 'payload', payload)
        setattr(transaction.data, 'payload_type', payload_type.get_type)
        self.data = transaction.data

    def from_proto(self, msg: bytes):
        transaction = transaction_pb2.Transaction()
        transaction.ParseFromString(msg)
        self.hash = bytearray(transaction.hash)
        self.from_addr = Address.parse_from_bytes(bytearray(getattr(transaction, "from")))
        self.chain_id = transaction.chain_id
        self.gas_price = ByteUtils.bytes2integer(bytearray(transaction.gas_price))
        self.gas_limit = ByteUtils.bytes2integer(bytearray(transaction.gas_limit))
        self.nonce = transaction.nonce
        self.alg = Algorithm(transaction.alg)
        self.sign = transaction.sign
        self.timestamp = transaction.timestamp
        self.to_addr = Address.parse_from_bytes(bytearray(getattr(transaction, "to")))
        self.value = ByteUtils.bytes2integer(bytearray(transaction.value))

        if transaction.data is None:
            raise Exception("invalid transaction data")

        if len(bytearray(transaction.data.payload)) > self.__MaxDataPayLoadLength:
            raise Exception("payload data length is out of max length")

        self.data = transaction.data

    def to_proto(self) -> str:
        transaction = transaction_pb2.Transaction()
        setattr(transaction, 'alg', self.alg.get_type)
        setattr(transaction, 'chain_id', self.chain_id)
        setattr(transaction, 'from', bytes(self.from_addr.bytes()))
        setattr(transaction, 'to', bytes(self.to_addr.bytes()))
        setattr(transaction, 'value', ByteUtils.integer2bytes(self.value))
        setattr(transaction, 'gas_limit', ByteUtils.integer2bytes(self.gas_limit))
        setattr(transaction, 'gas_price', ByteUtils.integer2bytes(self.gas_price))
        setattr(transaction, 'nonce', self.nonce)
        setattr(transaction, 'hash', bytes(self.hash))
        setattr(transaction, 'sign', self.sign)
        setattr(transaction, 'timestamp', self.timestamp)
        setattr(transaction.data, 'payload', self.data.payload)
        setattr(transaction.data, 'payload_type', self.data.payload_type)

        '''
        print(transaction)
        print(transaction.alg == self.orgtx.alg)
        print(transaction.chain_id == self.orgtx.chain_id)
        print(getattr(transaction, "from") == getattr(self.orgtx, "from"))
        print(getattr(transaction, "to") == getattr(self.orgtx, "to"))
        print(transaction.value == self.orgtx.value)
        print(transaction.gas_limit == self.orgtx.gas_limit)
        print(transaction.gas_price == self.orgtx.gas_price)
        print("nonce")
        print(transaction.nonce == self.orgtx.nonce)
        print(transaction.hash == self.orgtx.hash)
        print(transaction.sign == self.orgtx.sign)
        print(transaction.timestamp == self.orgtx.timestamp)
        print(transaction.data == self.orgtx.data)
        '''
        return base64.b64encode(transaction.SerializeToString()).decode("utf-8")

    def calculate_hash(self):
        hash = Hash.sha3256(
                        bytes(self.from_addr.bytes()),
                        bytes(self.to_addr.bytes()),
            ByteUtils.integer2bytes(self.value),
            ByteUtils.long2bytes(self.nonce),
            ByteUtils.long2bytes(self.timestamp),
            self.data.SerializeToString(),
            ByteUtils.int2bytes(self.chain_id),
            ByteUtils.integer2bytes(self.gas_price),
            ByteUtils.integer2bytes(self.gas_limit)
                         )
        self.hash = hash
        return self.hash

    def sign_hash(self):
        signature = ECsignature()
        pri_key = self.__from_account.get_private_key_obj()
        signature.init_sign(pri_key)
        sign = signature.sign(self.hash)
        self.alg = Algorithm(signature.algorithm())
        self.sign = sign.to_bytes()

