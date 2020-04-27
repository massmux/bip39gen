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
import random,string

""" parsing arguments """
parser = argparse.ArgumentParser("bip39gen")
parser.add_argument("-p","--passphrase", help="The optional bip39 passphrase", type=str, required=False)
parser.add_argument("-e","--entropy", help="The optional entropy provided by the user", type=str, required=False)
args = parser.parse_args()

oPassphrase=args.passphrase
oEntropy=args.entropy

""" create 32 letters random string """
def getRandom(stringLength=32):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


mnemo = Mnemonic('english')

""" check if entropy provided, otherwise internal random """
if oEntropy:
    pass
else:
    oEntropy=getRandom(32)

""" create bip39 24 words """
entropy_b = bytearray(str(oEntropy), 'utf-8')
entropy_hash =hashlib.sha256(entropy_b).digest()
entropy = hexlify(entropy_hash)
words = mnemo.to_mnemonic(entropy_hash)

if oPassphrase:
    passphrase=oPassphrase
else:
    passphrase=""

""" calc seed from mnemonic and passphrase """
seed=hexlify(Mnemonic.to_seed(words, passphrase))

""" print results"""
print("[Entropy]\n%s" % entropy)
print("[Words]\n%s" % words)
print("[Passphrase]\n%s" % passphrase)
print("[Seed]\n%s" % str(seed))

