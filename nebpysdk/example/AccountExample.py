# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 下午3:30
# @Author  : GuoXiaoMin
# @File    : AccountExample.py
# @Software: PyCharm

from nebpysdk.src.account.Account import Account

# generate a new account
# account = Account.new_account()

account = Account.new_account()
print("new account", account.get_address_str())

account = Account()
print("new account", account.get_address_str())

account = Account.new_account("6c41a31b4e689e1441c930ce4c34b74cc037bd5e68bbd6878adb2facf62aa7f3")
print("new account with given priv_key", account.get_address_str())
account = Account.new_account(bytes.fromhex("6c41a31b4e689e1441c930ce4c34b74cc037bd5e68bbd6878adb2facf62aa7f3"))
print("new account with given priv_key", account.get_address_str())

account = Account("6c41a31b4e689e1441c930ce4c34b74cc037bd5e68bbd6878adb2facf62aa7f3")
print("new account with given priv_key", account.get_address_str())

# export account
account_json = account.to_key("passphrase")
print(account_json)

# load account
account = Account.from_key(account_json, "passphrase".encode())
print(account.get_address_str())
print(account.get_private_key())
print(account.get_public_key())