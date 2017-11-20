#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 00:40:53 2017

@author: parth
"""
import csv
import sys
# For doing cool regular expressions
import re
import time
# For sorting dictionaries
import operator
import pandas as pd
import numpy as np
from textblob import TextBlob
test_df=pd.read_csv('test.csv',encoding = "ISO-8859-1") 
use=test_df["ItemID"]
test_df=test_df["SentimentText"]
#print(test_df)
polarity=[]
def tweets():
    for row in test_df:

            tweet=row
        
        
#        tweet['orig'] = row[2]
#        print(tweet['orig'])
#        tweet['id'] = int(row[0])
#        tweet['pubdate'] = time.strftime('%Y/%m/%d', time.strptime(row[1],'%a %b %d %H:%M:%S +0000 %Y'))
#

#        if re.match(r'^RT.*', tweet['orig']):
#            continue
#
#        tweet['clean'] = tweet['orig']
#
#        # Remove all non-ascii characters
#        tweet['clean'] = strip_non_ascii(tweet['clean'])
#
#        # Remove URLS. (I stole this regex from the internet.)
#        tweet['clean'] = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet['clean'])
#
#        # Fix classic tweet lingo
#        tweet['clean'] = re.sub(r'\bthats\b', 'that is', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bive\b', 'i have', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bim\b', 'i am', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bya\b', 'yeah', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bcant\b', 'can not', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bwont\b', 'will not', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bid\b', 'i would', tweet['clean'])
#        tweet['clean'] = re.sub(r'wtf', 'what the fuck', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bwth\b', 'what the hell', tweet['clean'])
#        tweet['clean'] = re.sub(r'\br\b', 'are', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bu\b', 'you', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bk\b', 'OK', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bsux\b', 'sucks', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bno+\b', 'no', tweet['clean'])
#        tweet['clean'] = re.sub(r'\bcoo+\b', 'cool', tweet['clean'])
#        tweet['clean'] = re.sub(r'\\n', ' ', tweet['clean'])
#        tweet['clean'] = re.sub(r'\\r', ' ', tweet['clean'])
#        tweet['clean'] = re.sub(r'&gt;', '', tweet['clean'])
#        tweet['clean'] = re.sub(r'&amp;', 'and', tweet['clean'])
#        tweet['clean'] = re.sub(r'\$ *hit', 'shit', tweet['clean'])
#        tweet['clean'] = re.sub(r' w\/', 'with', tweet['clean'])
#        tweet['clean'] = re.sub(r'\ddelay', '\d delay', tweet['clean'])

#         Create textblob object
            tweet = TextBlob(tweet)
            polr=float(tweet.sentiment.polarity)
            if(polr<=0):
                polr=0
            elif(polr>0):
                polr=1
#            elif(polr>-0.1 and polr<0.1):
#                polr=0
            polarity.append(polr)
    return polarity    
list=tweets()
df= pd.DataFrame({'header': list})
print(df)
submission = pd.DataFrame({
        "id": use,
        "polarity": list
    })
submission.to_csv('submissioncomp.csv', index=False)
        # Correct spelling (WARNING: SLOW)
        #tweet['TextBlob'] = tweet['TextBlob'].correct()
