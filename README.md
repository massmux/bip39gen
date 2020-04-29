# bip39gen
Generate bip39 mnemonic and seed

 from the command line you can generate a 24 words bip39 mnemonic from a random of your choice or with random from audio recording. Also a passphrase can be provided in order to have the bip39 seed correctly generated from mnemonic.

 the command is totally offline and can be run without any connection to the internet. It is better infact to run on a tails OS with internet disconnected and immediately save produced bip39 mnemonic on a sheet of paper.


 syntax

```
without params, creates mnemonic by gathering mic audio as entropy

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
 
 example, generate 24 words bip39 mnemonic with internal generation of entropy. Seed created with a passphrase provided

```
 ./bip39gen.py -p 1234
```
 
 example, generate 24 words bip39 mnemonic with a provided string as entropy. Seed created with the passphrase provided

```
 ./bip39gen.py -e 12345678 -p 1234

```



