# Copyright (C) 2011 Sam Rushing
# Copyright (C) 2013-2014 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

"""Base58 encoding and decoding"""

from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import binascii
b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


class Base58:

    @classmethod
    def encode(cls, b):
        """Encode bytes to a base58-encoded string"""

        # Convert big-endian bytes to integer
        n = int('0x0' + binascii.hexlify(b).decode('utf8'), 16)

        # Divide that integer into bas58
        res = []
        while n > 0:
            n, r = divmod(n, 58)
            res.append(b58_digits[r])
        res = ''.join(res[::-1])

        # Encode leading zeros as base58 zeros
        czero = b'\x00'
        if sys.version > '3':
            # In Python3 indexing a bytes returns numbers, not characters.
            czero = 0
        pad = 0
        for c in b:
            if c == czero:
                pad += 1
            else:
                break
        return b58_digits[0] * pad + res

    @classmethod
    def decode(cls, s):
        """Decode a base58-encoding string, returning bytes"""
        if not s:
            return b''

        # Convert the string to an integer
        n = 0
        for c in s:
            n *= 58
            if c not in b58_digits:
                raise Exception('Character %r is not a valid base58 character' % c)
            digit = b58_digits.index(c)
            n += digit

        # Convert the integer to bytes
        h = '%x' % n
        if len(h) % 2:
            h = '0' + h
        res = binascii.unhexlify(h.encode('utf8'))

        # Add padding back.
        pad = 0
        for c in s[:-1]:
            if c == b58_digits[0]:
                pad += 1
            else:
                break
        return b'\x00' * pad + res
