# bip39gen
Generate bip39 mnemonic and seed

 from the command line you can generate a 24 words bip39 mnemonic from a random of your choice or you can use the internal random generator. Also a passphrase can be provided in order to have the bip39 seed correctly generated from mnemonic.

 the command is totally offline and can be run without any connection to the internet. It is better infact to run on a tails OS with internet disconnected and immediately save produced bip39 mnemonic on a sheet of paper.

 to get more entropy you can generate an audiofile from mic and use it to create entropy (please see audgen.py script)


## bip39gen

 syntax

```
usage: bip39gen.py [-h] [-p PASSPHRASE] [-e ENTROPY]

optional arguments:
  -h, --help            show this help message and exit
  -p PASSPHRASE, --passphrase PASSPHRASE
                        The optional bip39 passphrase
  -e ENTROPY, --entropy ENTROPY
                        An optional random string or file=filename to get
                        entropy from file (example audio)

```

 example, generate 24 words bip39 mnemonic with internal generation of entropy. Seed created with no passphrase provided

```
 ./bip39gen.py
```
 
 example, generate 24 words bip39 mnemonic with a provided string as entropy. Seed created with no passphrase provided

```
 ./bip39gen.py -e 12345678
```

 example, generate 24 words bip39 mnemonic with a provided file (example audio) recorded with the audgen.py script included

```
 ./bip39gen.py -e file=audiofile.wav
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

 creates an audiofile from the mic

```
usage: audgen.py [-h] -f FILENAME [-l LENGTH]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Audio filename
  -l LENGTH, --length LENGTH
                        Audio recording length (default=3 sec)

```


