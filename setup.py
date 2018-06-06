# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 下午5:18
# @Author  : GuoXiaoMin
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup, find_packages

setup(
    name='NebulasSdkPy',
    version='0.3.0',
    author='GuoXiaoMin',
    packages=find_packages(exclude=["test", "test.*"]),
    url='',
    license='LICENSE.txt',
    description='NebulasSdkPy',
    #long_description=open('README.md').read(),
    install_requires=[
        "certifi == 2018.4.16",
        "chardet == 3.0.4",
        "Crypto == 1.4.1",
        "cytoolz == 0.9.0.1",
        "eth-hash == 0.1.3",
        "eth-keyfile == 0.5.1",
        "eth-keys == 0.2.0b3",
        "eth-utils == 1.0.3",
        "idna == 2.6",
        "Naked == 0.1.31",
        "protobuf == 3.5.2.post1",
        "pycryptodome == 3.6.1",
        "pycurl == 7.43.0.1",
        "pyscrypt == 1.6.2",
        "pysha3 == 1.0.2",
        "PyYAML == 3.12",
        "requests == 2.18.4",
        "sha3 == 0.2.1",
        "shellescape == 3.4.1",
        "six == 1.11.0",
        "toolz == 0.9.0",
        "urllib3 == 1.22"
    ],
)