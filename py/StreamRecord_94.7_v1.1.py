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

os.chdir("/home/AdSkipper/py/mp3_947")


while 1!=2:
    for i in range(0,21):
        stream_url = 'http://208.80.52.113/WLSFMAAC_SC'
        r = requests.get(stream_url, stream=True)
        sleep(4) #40

        idx = 0
        with open('radio1_stream'+str(i)+'.mp3', 'wb') as f:
                for block in r.iter_content(16): #32
                    idx += 1
                    f.write(block)
                    if(idx==3000): #10000
                        print(i)
                        break
        if os.path.isfile('/home/AdSkipper/py/wav947/radio1_stream'+str(i)+'.wav') :
            os.remove('/home/AdSkipper/py/wav947/radio1_stream'+str(i)+'.wav')
        call(["avconv", "-i", "radio1_stream"+str(i)+".mp3","/home/AdSkipper/py/wav947/radio1_stream"+str(i)+".wav"])

