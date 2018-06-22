#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:02:34 2018

@author: ajit
"""
'''
import vlc
p = vlc.MediaPlayer("http://your_mp3_url")
p.play()

important links:
https://stackoverflow.com/questions/4247248/record-streaming-and-saving-internet-radio-in-python
https://github.com/DirkR/podhorst
https://github.com/beedaddy/radiorec
http://people.csail.mit.edu/hubert/pyaudio/#docs
https://stackoverflow.com/questions/892199/detect-record-audio-in-python
http://python-sounddevice.readthedocs.io/en/0.3.10/

'''

import os
import requests
from time import sleep
from subprocess import call
#import pydub
#from pydub.utils import which
#pydub.AudioSegment.converter = which("ffmpeg")

#os.chdir("/home/ajit/Documents/adskipper/LiveRadioStreams/Radio_99.5/mp3")
os.chdir("/home/AdSkipper/py/mp3")

while 1!=2:
    for i in range(0,21):
        stream_url = 'http://14833.live.streamtheworld.com/WUSNFMAAC_SC'
        r = requests.get(stream_url, stream=True)
        sleep(4)

        idx = 0
        with open('radio1_stream'+str(i)+'.mp3', 'wb') as f:
            #16
                for block in r.iter_content(16):
                    idx += 1
                    f.write(block)
                    #3000
                    if(idx==3000):
                        print(i)
                        break
        if os.path.isfile('/home/AdSkipper/py/wav/radio1_stream'+str(i)+'.wav') :
            os.remove('/home/AdSkipper/py/wav/radio1_stream'+str(i)+'.wav')
        call(["avconv", "-i", "radio1_stream"+str(i)+".mp3","/home/AdSkipper/py/wav/radio1_stream"+str(i)+".wav"])

        #subprocess.call(["../ffmpeg-git-20180308-64bit-static/./ffmpeg", "-i", "radio1_stream"+str(i)+".mp3","/home/AdSkipper/py/wav/radio1_stream"+str(i)+".wav"])
        #sound = pydub.AudioSegment.from_mp3("radio1_stream"+str(i)+".mp3")
        #sound = pydub.AudioSegment.from_file("radio1_stream"+str(i)+".mp3", format="mp3")
        #sound.export("/home/AdSkipper/py/wav/radio1_stream"+str(i)+".wav", format="wav",parameters=["-q:a", "0"])

