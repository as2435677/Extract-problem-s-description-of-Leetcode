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
#driver.get('http://pala.tw/js-example/')
#pageSource = driver.page_source


def sleeptime(hour, minute, sec):
    return hour*3600 + minute*60 + sec

s_time = time.time()
fp = open("Href_list.txt", "w+")
link = "https://leetcode.com/problemset/all/"
driver.get(link)
#ps = driver.page_source
#soup = BeautifulSoup(ps, "html.parser")

i = 1
page = 1
total_problems = 0
while page<=33:
    if i == 1:
        ps = driver.page_source
        soup = BeautifulSoup(ps, "html.parser")
    items = soup.select("#question-app > div > div:nth-child(2) > div.question-list-base > div.table-responsive.question-list-table > table > tbody.reactable-data > tr:nth-child(" + str(i) + ") > td:nth-child(3) > div > a")
    for item in items:
        href = item.get('href')
    fp.write(href)
    fp.write("\n")
    #time.sleep(sleeptime(0,0,1))
    i = i + 1
    if i == 51:
        i = 1
        page = page + 1
        next_page = driver.find_element_by_class_name("reactable-next-page")
        next_page.click()
        time.sleep(sleeptime(0,0,1))
    total_problems = total_problems + 1
    if total_problems == 1649:
        break

fp.close()
driver.close()


