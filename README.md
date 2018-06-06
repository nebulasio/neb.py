# neb.py

neb.py is the Nebulas compatible Python API.
Users can sign/send transactions and deploy/call smart contract with it.

## Installation

You can install this library via pip:
```sh
pip install NebulasSdkPy
```

## Usage

please refer to [examples](/nebpysdk/example) to learn how to use neb.py.

#### Account

```
from nebpysdk.src.account.Account import Account
# generate a new account
account = Account.new_account()

# export account
account_json = account.to_key(bytes("passphrase".encode()))
print(account_json)

# load account
account = Account.from_key(account_json, bytes("passphrase".encode()))
print(account.get_address_str())
print(account.get_private_key())
print(account.get_public_key())

```

#### API

```
from nebpysdk.src.client.Neb import Neb
import json
neb = Neb()

# getNebState
print(neb.api.getNebState().text)

# latestIrreversibleBlock
print(neb.api.latestIrreversibleBlock().text)
```

#### Transaction

```
from nebpysdk.src.account.Account import Account
from nebpysdk.src.core.Address import Address
from nebpysdk.src.core.Transaction import Transaction
from nebpysdk.src.core.TransactionBinaryPayload import TransactionBinaryPayload
from nebpysdk.src.core.TransactionCallPayload import TransactionCallPayload
from nebpysdk.src.client.Neb import Neb
import json

neb = Neb()
keyJson = '{"version":4,"id":"814745d0-9200-42bd-a4df-557b2d7e1d8b","address":"n1H2Yb5Q6ZfKvs61htVSV4b1U2gr2GA9vo6","crypto":{"ciphertext":"fb831107ce71ed9064fca0de8d514d7b2ba0aa03aa4fa6302d09fdfdfad23a18","cipherparams":{"iv":"fb65caf32f4dbb2593e36b02c07b8484"},"cipher":"aes-128-ctr","kdf":"scrypt","kdfparams":{"dklen":32,"salt":"dddc4f9b3e2079b5cc65d82d4f9ecf27da6ec86770cb627a19bc76d094bf9472","n":4096,"r":8,"p":1},"mac":"1a66d8e18d10404440d2762c0d59d0ce9e12a4bbdfc03323736a435a0761ee23","machash":"sha3256"}}';
password = 'passphrase'

# prepare from&to addr
from_account = Account.from_key(keyJson, bytes(password.encode()))
from_addr = from_account.get_address_obj()
to_addr = Address.parse_from_string("n1JmhE82GNjdZPNZr6dgUuSfzy2WRwmD9zy")
print("from_addr", from_addr.string())
print("to_addr  ", to_addr.string())

# prepare transaction, get nonce first
resp = neb.api.getAccountState(from_addr.string()).text

print(resp)
resp_json = json.loads(resp)
print(resp_json)
nonce = int(resp_json['result']['nonce'])

chain_id = 1001
# PayloadType
payload_type = Transaction.PayloadType("binary")
# payload
payload = TransactionBinaryPayload("test").to_bytes()
# gasPrice
gas_price = 1000000
# gasLimit
gas_limit = 20000

# binary transaction example
tx = Transaction(chain_id, from_account, to_addr, 0, nonce + 1, payload_type, payload, gas_price, gas_limit)
tx.calculate_hash()
tx.sign_hash()
print(neb.api.sendRawTransaction(tx.to_proto()).text)


# call type
to_addr = Address.parse_from_string("n1oXdmwuo5jJRExnZR5rbceMEyzRsPeALgm")
func = "get"
arg = '["nebulas"]'
payload = TransactionCallPayload(func, arg).to_bytes()
payload_type = Transaction.PayloadType("call")
tx = Transaction(chain_id, from_account, to_addr, 0, nonce + 1, payload_type, payload, gas_price, gas_limit)
tx.calculate_hash()
tx.sign_hash()
print(neb.api.sendRawTransaction(tx.to_proto()).text)

```

## Join in!

We are happy to receive bug reports, fixes, documentation enhancements, and other improvements.

Please report bugs via the github issue

