#!/usr/bin/python3

"""
This script gather an audio file from mic and creates a file. Used to create entropy
"""

import argparse
import sounddevice as sd
from scipy.io.wavfile import write

""" parsing arguments """
parser = argparse.ArgumentParser("audgen.py")
parser.add_argument("-f","--filename", help="Audio filename", type=str, required=True)
parser.add_argument("-l","--length", help="Audio recording length (default=3 sec)", type=int, default=3,required=False)
args = parser.parse_args()

oFilename=args.filename
oSamplerate=44100
oLength=args.length

myRec = sd.rec(int(oLength * oSamplerate), samplerate=oSamplerate, channels=2)
sd.wait()
write(oFilename, oSamplerate, myRec) 

