#!/usr/bin/python3


#   Copyright (C) 2019-2020 Denali Sàrl www.denali.swiss, Massimo Musumeci, @massmux
#
#   This file is a script to calculate bip39 24 words mnemonic by mic gathered randomness
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
from mnemonic import Mnemonic
from binascii import hexlify, unhexlify
import argparse
import subprocess

rnd_len=4

""" parsing arguments """
parser = argparse.ArgumentParser("bip39gen.py")
parser.add_argument("-p","--passphrase", help="The optional bip39 passphrase", type=str, required=False)
parser.add_argument("-e","--entropy", help="An optional random string \
                    in case you prefer providing your own entropy", type=str, required=False)
args = parser.parse_args()
(oPassphrase,oEntropy)=(args.passphrase,args.entropy)

mnemo = Mnemonic('english')
""" check if entropy provided, otherwise use random from mic recording """
fileContent=""
if oEntropy:
    # accept and use entropy string provided by user
    print("You provided the entropy as a string")
    entropy_b = bytearray(str(oEntropy), 'utf-8')
else:
    # create random by reading the mic
    print("Creating entropy from %s secs mic audiorecording.. please wait" % str(rnd_len) )
    mycmd=subprocess.getoutput('arecord -d %s -f dat -t wav -q | sha256sum -b' %  str(rnd_len) )
    print("Generated 256bits entropy: %s" % mycmd[:64])
    entropy_b = bytearray(mycmd[:64], 'utf-8')

""" create bip39 24 words """
entropy_hash =hashlib.sha256(entropy_b).digest()
entropy = hexlify(entropy_hash)
words = mnemo.to_mnemonic(entropy_hash)
words_arr=words.split(" ")
passphrase = oPassphrase or ""
""" calc seed from mnemonic and passphrase """
seed=hexlify(Mnemonic.to_seed(words, passphrase))

""" print results"""
print("BIP39 words sequence")
n=1
for i in words_arr:
    print("word %s\t: %s" % (n,i) )
    n+=1
if passphrase:
    print("passph\t: %s" % passphrase)
print("seed\t: %s\n" % str(seed))

