from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='neb-py',
    version='0.4.4',
    author='Zhuoer Wang',
    packages=find_packages(exclude=["test", "test.*"]),
    license='LICENSE.txt',
    description='Nebulas Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nebulasio/neb.py",
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
        "pycryptodome == 3.6.6",
        "pycurl == 7.43.0.1",
        "pyscrypt == 1.6.2",
        "pysha3 == 1.0.2",
        "PyYAML == 5.4",
        "requests == 2.18.4",
        "shellescape == 3.4.1",
        "six == 1.11.0",
        "toolz == 0.9.0",
        "urllib3 == 1.22"
    ],
)
