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
import argparse,os,subprocess

""" check if sounddevice lib is available, if it is then gets imported """
try:
    import sounddevice
    mode='sd'
except ImportError:
    mode='arec'

""" system constants """

NOISE_SAMPLE        = 5    # main sampling seconds
SHA256_ROUNDS       = 2048  # sha256 rounds (number)
NOISE_SAMPLE_SALT   = 3     # salt sampling seconds
SAMPLE_RATE         = 44100 # samplerate
SAMPLING_FMT        = 'wav'


""" parsing arguments """
def parseArguments():
    global args
    parser = argparse.ArgumentParser("bip39gen.py")
    parser.add_argument("-e","--entropy", help="An optional random string \
                        in case you prefer providing your own entropy", type=str, required=False)
    args = parser.parse_args()

""" hash assist """
def getsha256(z):
    return hashlib.sha256(z.encode('utf-8')).hexdigest()

""" elaborate words for printing """
def showResults(words):
    words_arr=words.split(" ")
    print("**BIP39 words generated sequence**")
    n=1
    for i in words_arr:
        print ("{:12}: {:12}".format(n, i))
        n+=1
    print("BIP39 words generated sequence - single line print")
    print(words)
    return

def getRandNoise():
    """
    creating unique noise by sampling entropy and salting it for SHA256_ROUNDS / use arecord+sha256 OS commands
    this function is better when no equivalent library is available. Returns sha256 salt hashed noise
    """
    mycmd=subprocess.getoutput('arecord -d %s -f dat -t %s -q | sha256sum -b' %  (str(NOISE_SAMPLE),SAMPLING_FMT ))
    hash0=mycmd[:64]
    mysalt=subprocess.getoutput('arecord -d %s -f dat -t %s -q | sha256sum -b' %  (str(NOISE_SAMPLE_SALT),SAMPLING_FMT ))
    salt0=mysalt[:64]
    for i in range(0,SHA256_ROUNDS):
        hash0=getsha256(hash0+salt0)
    return hash0

def getNoise256():
    """
    creating unique noise by sampling entropy and salting it for SHA256_ROUNDS / use python lib
    Returns sha256 salt hashed noise
    """
    noise0 = sounddevice.rec(int(SAMPLE_RATE * NOISE_SAMPLE), samplerate=SAMPLE_RATE, channels=2, blocking=True)
    salt0 = sounddevice.rec(int(SAMPLE_RATE * NOISE_SAMPLE_SALT), samplerate=SAMPLE_RATE, channels=2, blocking=True)
    (noise,salt) =( hashlib.sha256(bytearray(b''.join(noise0))).hexdigest() , hashlib.sha256(bytearray(b''.join(salt0))).hexdigest() )
    for i in range(0,SHA256_ROUNDS):
        noise=getsha256(noise+salt)
    return noise

def clear():
    """ clears screen """
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def main():
    oEntropy=args.entropy
    mnemo = Mnemonic('english')
    """ check if entropy provided, otherwise use random from mic recording """
    fileContent=""
    if oEntropy:
        # accept and use entropy string provided by user instead of mic one
        print("You provided the entropy as a string")
        hash0=getsha256(oEntropy)
        print("256bits hash from your source: %s" % hash0)
    else:
        print("Getting entropy from %s secs mic audiorecording.. please wait" % str(NOISE_SAMPLE) )
        hash0=getRandNoise() if mode=='arec' else getNoise256()

    entropy_b = bytearray(hash0, 'utf-8')
    """ create bip39 24 words """
    entropy_hash =hashlib.sha256(entropy_b).digest()
    entropy = hexlify(entropy_hash)
    words = mnemo.to_mnemonic(entropy_hash)
    
    """ print results """
    clear()
    showResults(words)


if __name__ == "__main__":
    parseArguments()
    main()


