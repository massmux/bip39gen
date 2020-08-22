# bip39gen
Generate bip39 mnemonic and seed

 from the command line you can generate a 24 words bip39 mnemonic from randomness coming from the computer's mic (usage without the -e parameter) or by providing your own entropy source (using the -e par). The source of entropy is then hashed with a number of rounds.

 the command is totally offline and must be run on a clean computer without any connection to the internet. It is suggested for example to run on a Tails OS (or similar Linux flavor OS) with internet disconnected and immediately save produced bip39 mnemonic on a sheet of paper. Beware also that no external source is watching at the procedure (a camera for example).

 syntax

```
without params, creates mnemonic by gathering mic audio noise as a source of entropy. Here the command syntax:

usage: bip39gen.py [-h] [-e ENTROPY]

optional arguments:
  -h, --help            show this help message and exit
  -e ENTROPY, --entropy ENTROPY
                        An optional random string in case you prefer providing your own entropy

```

 example, generate 24 words bip39 mnemonic with entropy from microphone audio recording.

```
 ./bip39gen.py
```
 
 example, generate 24 words bip39 mnemonic with a provided string as entropy.

```
 ./bip39gen.py -e 12345678
```
 

 we talk about these topics on this youtube channel: http://www.youtube.com/c/MassimoSMusumeci and also at the telegram group: https://t.me/BitcoinSecPriv . Please refer also to website https://www.massmux.com for more infos.


