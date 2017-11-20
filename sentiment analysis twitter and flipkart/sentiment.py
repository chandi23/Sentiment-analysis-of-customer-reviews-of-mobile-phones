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
import matplotlib
import matplotlib.pyplot as plt

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
#        tweet = tweet['orig']
#
#        # Remove all non-ascii characters
#        tweet = strip_non_ascii(tweet)
#
#        # Remove URLS. (I stole this regex from the internet.)
#        tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet)
#
#        # Fix classic tweet lingo
            tweet = re.sub(r'\bthats\b', 'that is', tweet)
            tweet = re.sub(r'\bive\b', 'i have', tweet)
            tweet = re.sub(r'\bim\b', 'i am', tweet)
            tweet = re.sub(r'\bya\b', 'yeah', tweet)
            tweet = re.sub(r'\bcant\b', 'can not', tweet)
            tweet = re.sub(r'\bwont\b', 'will not', tweet)
            tweet = re.sub(r'\bid\b', 'i would', tweet)
            tweet = re.sub(r'wtf', 'what the fuck', tweet)
            tweet = re.sub(r'\bwth\b', 'what the hell', tweet)
            tweet = re.sub(r'\br\b', 'are', tweet)
            tweet = re.sub(r'\bu\b', 'you', tweet)
            tweet = re.sub(r'\bk\b', 'OK', tweet)
            tweet = re.sub(r'\bsux\b', 'sucks', tweet)
            tweet = re.sub(r'\bno+\b', 'no', tweet)
            tweet = re.sub(r'\bcoo+\b', 'cool', tweet)
            tweet = re.sub(r'\\n', ' ', tweet)
            tweet = re.sub(r'\\r', ' ', tweet)
            tweet = re.sub(r'&gt;', '', tweet)
            tweet = re.sub(r'&amp;', 'and', tweet)
            tweet = re.sub(r'\$ *hit', 'shit', tweet)
            tweet = re.sub(r' w\/', 'with', tweet)
            tweet = re.sub(r'\ddelay', '\d delay', tweet)
            tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet)

#         Create textblob object
            tweet = TextBlob(tweet)
            polr=float(tweet.sentiment.polarity)
            polr=polr*10
            polr=polr+10
#            if(polr<=-0.1):
#                polr=-1
#            elif(polr>=0.1):
#                polr=1
#            elif(polr>-0.1 and polr<0.1):
#                polr=0
            polarity.append(polr)
    return polarity    
list=tweets()
df= pd.DataFrame({'header': list})
#print(df)
df.plot(kind='line')
#submission = pd.DataFrame({
#        "id": use,
#        "trip_duration": list
#    })
#print(submission)
        # Correct spelling (WARNING: SLOW)
        #tweet['TextBlob'] = tweet['TextBlob'].correct()
