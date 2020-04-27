#!/usr/bin/python3


#   Copyright (C) 2019-2020 Denali Sàrl www.denali.swiss, Massimo Musumeci, @massmux
#
#   This file is part of btcnode bot, a telegram bot which interacts with bitcoin core node.
#
#   It is subject to the license terms in the LICENSE file found in the top-level
#   directory of this distribution.
#
#   No part of this software, including this file, may be copied, modified,
#   propagated, or distributed except according to the terms contained in the
#   LICENSE file.
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER


import hashlib
import sys
from mnemonic import Mnemonic
from binascii import hexlify, unhexlify
import argparse
import random

# parsing arguments

parser = argparse.ArgumentParser("bip39gen")
parser.add_argument("-p","--passphrase", help="The optional bip39 passphrase", type=str, required=False)
parser.add_argument("-e","--entropy", help="The optional entropy provided by the user", type=str, required=False)
args = parser.parse_args()

oPassphrase=args.passphrase
oEntropy=args.entropy

mnemo = Mnemonic('english')

if oEntropy:
    pass
else:
    oEntropy=random.randint(1,9999999999999999999999999999999999999)

entropy_b = bytearray(str(oEntropy), 'utf-8')
entropy_hash =hashlib.sha256(entropy_b).digest()
entropy = hexlify(entropy_hash)
##words = mnemo.to_mnemonic(unhexlify(entropy))

words = mnemo.to_mnemonic(entropy_hash)

if oPassphrase:
    passphrase=oPassphrase
else:
    passphrase=""

seed=hexlify(Mnemonic.to_seed(words, passphrase))

print("Entropy: %s" % entropy)
print("Words: %s" % words)
print("Passphrase: %s" % str(passphrase))
print("Seed: %s" % str(seed))

