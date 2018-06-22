#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 01:39:45 2018

@author: ajit
"""

import os
import time, sys
#import urllib2
import urllib.request

os.chdir('/home/AdSkipper/py/wav')

url = "http://14833.live.streamtheworld.com/WUSNFMAAC_SC"
#print ("Connecting to "+url)

while True:
    for i in range(21):
        response = urllib.request.urlopen(url, timeout=8)
        fname = "radio1_stream"+str(i)+".wav"
        f = open(fname, 'wb')
        block_size = 12
        #print ("Recording roughly 6 seconds of audio Now - Please wait")
        limit = 6
        start = time.time()
        while time.time() - start < limit:
            try:
                audio = response.read(block_size)
                if not audio:
                    break
                f.write(audio)
                #sys.stdout.write('.')
                sys.stdout.flush()
            except Exception as e:
                print ("Error "+str(e))
        f.close()
        sys.stdout.flush()
        #print("")
        #print ("6 seconds from "+url+" have been recorded in "+fname)
