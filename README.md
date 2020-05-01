# bip39gen
Generate bip39 mnemonic and seed

 from the command line you can generate a 24 words bip39 mnemonic from randomness coming from the computer's mic (usage without the -e parameter) or by providing your own entropy source (using the -e par). Also a passphrase can be provided in order to have the bip39 seed correctly generated from mnemonic.

 the command is totally offline and can be run without any connection to the internet. It is very important infact to run on a Tails OS (or similar Linux flavor OS) with internet disconnected and immediately save produced bip39 mnemonic on a sheet of paper. Beware also that no external source is watching at the procedure (a camera for example).


 syntax

```
without params, creates mnemonic by gathering mic audio noise as entropy

usage: bip39gen.py [-h] [-p PASSPHRASE] [-e ENTROPY]

optional arguments:
  -h, --help            show this help message and exit
  -p PASSPHRASE, --passphrase PASSPHRASE
                        The optional bip39 passphrase
  -e ENTROPY, --entropy ENTROPY
                        An optional random string

```

 example, generate 24 words bip39 mnemonic with entropy from microphone audio recording. Seed created with no passphrase provided

```
 ./bip39gen.py
```
 
 example, generate 24 words bip39 mnemonic with a provided string as entropy. Seed created with no passphrase provided

```
 ./bip39gen.py -e 12345678
```
 
 example, generate 24 words bip39 mnemonic with internal generation of entropy (by mic). Seed created with a passphrase provided

```
 ./bip39gen.py -p 1234
```
 
 example, generate 24 words bip39 mnemonic with a provided string as entropy (this can be a sha256 entry from hashing some random source). Seed created with the passphrase provided

```
 ./bip39gen.py -e 12345678 -p 1234

```

 we talk about that on this video (italian): https://www.youtube.com/watch?v=coszyHeNlEg and also at the telegram group: https://t.me/BitcoinSecPriv


