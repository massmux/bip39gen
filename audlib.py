#!/usr/bin/python3

"""
This script gather an audio file from mic and creates a file. Used to create entropy
"""

import argparse
import sounddevice as sd
from scipy.io.wavfile import write


def getAudio(oFilename,oSamplerate=44100,oLength=3):
    myRec = sd.rec(int(oLength * oSamplerate), samplerate=oSamplerate, channels=2)
    sd.wait()
    write(oFilename, oSamplerate, myRec) 

