#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:19:56 2017

@author: rajat
"""
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from contextlib import closing
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re
import sys
import requests
from bs4 import BeautifulSoup
import unicodedata
from urllib.request import urlopen
import re

def remove_non_ascii_1(text):

    return ''.join([i if ord(i) < 128 else ' ' for i in text])

p_name = input("Enter a product name : ")


def uprint(*objects, sep=' ', end=' ', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get('http://www.flipkart.com/search?q='+p_name)
data = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
collection = soup.find_all("div", {"class": "col MP_3W3 _31eJXZ"})
href = []
for c in collection:
    a = c.find("a")
    href.append(a['href'])
product_href = href[0]
s1 = product_href[:product_href.rfind("&srno")]
p_id = s1.split("/p/")[1]

with closing(Firefox()) as browser:
    site = "https://www.flipkart.com/"+p_name+"/product-reviews/"+p_id
    browser.get(site)

    file = open("review.txt", "w")

    for count in range(1, 20):
        nav_btns = browser.find_elements_by_class_name('_33m_Yg')

        button = ""

        for btn in nav_btns:
            number = int(btn.text)
            if(number==count):
                button = btn
                break

        button.send_keys(Keys.RETURN)
        WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_2xg6Ul")))

        read_more_btns = browser.find_elements_by_class_name('_1EPkIx')


        for rm in read_more_btns:
            browser.execute_script("return arguments[0].scrollIntoView();", rm)
            browser.execute_script("window.scrollBy(0, -150);")
            rm.click()

        page_source = browser.page_source

        soup = BeautifulSoup(page_source, "lxml")
        ans = soup.find_all("div", class_="_3DCdKt")


        for tag in ans:
            title = str(tag.find("p", class_="_2xg6Ul").string).replace(u"\u2018", "'").replace(u"\u2019", "'")
            title = remove_non_ascii_1(title)
            title.encode('ascii','ignore')
            content = tag.find("div", class_="qwjRop").div.prettify().replace(u"\u2018", "'").replace(u"\u2019", "'")
            content = remove_non_ascii_1(content)
            content.encode('ascii','ignore')
            content = content[15:-7]
            content = re.compile(r'<[^>]+>').sub('', content)
            content = content.replace('\n', '')
            date = str(tag.find_all("p", class_="_3LYOAd"))
            date = re.compile(r'<[^>]+>').sub('', date)
       #    date = date.rsplit(']', 1)[0]
            date = date[:-1]

            votes = tag.find_all("span", class_="_1_BQL8")
            upvotes = int(votes[0].string)
            downvotes = int(votes[1].string)

        #    file.write("Review Title : %s\n\n" % title )
         #   file.write("Upvotes : " + str(upvotes) + "\n\nDownvotes : " + str(downvotes) + "\n\n")
            file.write("%s | " % content )
            file.write("%s\n\n" % date)
    file.close()

df=pd.read_table('review.txt', sep='|', header=None)
df.columns = ["Review", "Date"]    
df[['name', 'date', 'year']] = pd.DataFrame([ x.split(',') for x in df['Date'].tolist() ])
df = df.drop('name', 1)
df = df.drop('Date', 1)
df['Date'] = df['date'] + df['year']
df[['day', 'month']] = pd.DataFrame([ x.split() for x in df['date'].tolist() ])
df = df.drop('date', 1)
cols = list(df)
cols.insert(4, cols.pop(cols.index('year')))
df = df.loc[:, cols]
df.to_csv('flipkart_review.csv')
print("The customer reviews for %s have been scraped.." %p_name)

