# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 下午3:29
# @Author  : GuoXiaoMin
# @File    : ApiExample.py
# @Software: PyCharm
from nebpysdk.src.client.Neb import Neb
import json
neb = Neb("https://testnet.nebulas.io")

# getNebState
print(neb.api.getNebState().text)

# latestIrreversibleBlock
print(neb.api.latestIrreversibleBlock().text)

# getAccountState
print(neb.api.getAccountState("n1GDCCpQ2Z97o9vei2ajq6frrTPyLNCbnt7").text)

# getBlockByHash
print(neb.api.getBlockByHash("5cce7b5e719b5af679dbc0f4166e9c8665eb03704eb33b97ccb59d4e4ba14352").text)

# getBlockByHeight
print(neb.api.getBlockByHeight(1000).text)

# getBlockByHeight
print(neb.api.getBlockByHeight("1000").text)

# getTransactionReceipt
print(neb.api.getTransactionReceipt("8b98a5e4a27d2744a6295fe71e4f138d3e423ced11c81e201c12ac8379226ad1").text)

# getTransactionByContract
print(neb.api.getTransactionByContract("n1zRenwNRXVwY6akcF4rUNoKhmNWP9bhSq8").text)

# getAccountState
print(neb.api.getAccountState("n1GDCCpQ2Z97o9vei2ajq6frrTPyLNCbnt7").text)
re = json.loads(neb.api.getAccountState("n1GDCCpQ2Z97o9vei2ajq6frrTPyLNCbnt7").text)
print(re)

# call
re1 = neb.api.call("n1JmhE82GNjdZPNZr6dgUuSfzy2WRwmD9zy",
                    "n1JmhE82GNjdZPNZr6dgUuSfzy2WRwmD9zy",
                                                "100000",
                                                 "23",
                                                "200000",
                                                "200000").text
print(re1)
re1 = json.loads(re1)

re = neb.api.call("n1JmhE82GNjdZPNZr6dgUuSfzy2WRwmD9zy",
                    "n1zRenwNRXVwY6akcF4rUNoKhmNWP9bhSq8",
                                                "100000",
                                             int(re['result']['nonce']) + 1,
                                                "200000",
                                                "200000", {'function': 'getOrderCount', 'args': ''}).text
re = json.loads(re)
print(re)

# estimateGas
print(neb.api.estimateGas("n1JmhE82GNjdZPNZr6dgUuSfzy2WRwmD9zy",
                   "n1JmhE82GNjdZPNZr6dgUuSfzy2WRwmD9zy",
                   "100000",
                   "23",
                   "200000",
                   "200000").text)


# subscribe (define an event_subscriber to handle the subscribed events)
def event_subscriber(event):
    print(event)

neb.set_request("http://172.16.1.6:8685")  #use local nodes to test subscribe api
topics = ["chain.linkBlock", "chain.pendingTransaction","chain.newTailBlock"]
neb.api.subscribe(topics,event_subscriber)
