#!/usr/bin/env python
# encoding: utf-8
from textblob import TextBlob
import sys
import pandas as pd

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got
text=[]
mnth=[]
def main():

    def printTweet(descr, t, k):
        if(TextBlob(t.text).detect_language()=='en'):
            print(descr)
            print("Username: %s" % t.username)
            print("Month: %s" % t.date.month)
            print("Text: %s\n\n" % t.text)
            text.append(t.text)
            mnth.append(t.date.month)           
            k+=1
        return k;
        #print("language: %s\n\n\n" % TextBlob(t.text).detect_language())
        #print("Hastags: %s" % t.)
        #print("%b\n\n",)

    # Example 1 - Get tweets by username
    #tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
    #tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    #printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)
       
        month=1
    # Example 2 - Get tweets by query search
    while(month<=10):
        d1="2017-"+str(month)+"-1";
        d2="2017-"+str(month)+"-27";
        print("date: %s\n" %d1)
        i=0
        count=0
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch('iphone 7').setSince(d1).setUntil(d2).setMaxTweets(150)
        while (i<150 and count<50):
                tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
                s="ID: ",count;
                count=printTweet(s, tweet, count)
            #print(tweet)
                i+=1
        print("month: %d\n" %month) 
        month+=1
    # Example 3 - Get tweets by username and bound dates
    #tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
    #tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    #printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)
    df=pd.DataFrame({"text":text,"month":mnth})
    print(df)
    df.to_csv("~/iphone7.csv",encoding='utf-8')

if __name__ == '__main__':
    main()
