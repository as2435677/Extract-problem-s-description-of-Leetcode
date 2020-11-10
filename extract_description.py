#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:59:19 2020

@author: ken
"""

import requests as rq
from bs4 import BeautifulSoup
import io
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)



def sleeptime(hour, minute, sec):
    return hour*3600 + minute*60 + sec

#s_time = time.time()
fp = open("Href_list.txt", "r+")
#line = fp.readline()
#line = line[10:len(line)-1]
link = "https://leetcode.com/problems/"
#driver.get(link + line + "/")
#ps = driver.page_source
#soup = BeautifulSoup(ps, "html.parser")

while True:
    line = fp.readline()
    if line == '':
        break
    line = line[10:len(line)-1]
    #print(line)
    driver.get(link + line + "/")
    time.sleep(sleeptime(0,0,3))
    ps = driver.page_source
    soup = BeautifulSoup(ps, "html.parser")
    items = soup.select("#app > div > div.main__2_tD > div.content__3fR6 > div > div.side-tools-wrapper__1TS9 > div > div.css-9z7f7i-Container.e5i1odf0 > div.css-jtoecv > div > div.tab-pane__ncJk.css-xailxq-TabContent.e5i1odf5 > div > div.content__u3I1.question-content__JfgR")
    fo = open("/home/ken/leetcode_web_crawler/descriptions/" + line + ".txt", "w+")
    fo.writelines(["%s\n" % item  for item in items])
    fo.close()
    time.sleep(sleeptime(0,0,1))
    


fp.close()
driver.close()


