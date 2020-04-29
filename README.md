# bip39gen
Generate bip39 mnemonic and seed

 from the command line you can generate a 24 words bip39 mnemonic from a random of your choice or with random from audio recording. Also a passphrase can be provided in order to have the bip39 seed correctly generated from mnemonic.

 the command is totally offline and can be run without any connection to the internet. It is better infact to run on a tails OS with internet disconnected and immediately save produced bip39 mnemonic on a sheet of paper.


## bip39gen

 requirements (for audio)

```
 pip3 install sounddevice
 pip3 install scipy
```

 

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

## audiogen facility

 if you just want to create an audiofile from the mic, you can use this facility

```
usage: audgen.py [-h] -f FILENAME [-l LENGTH]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Audio filename
  -l LENGTH, --length LENGTH
                        Audio recording length (default=3 sec)

```


