# ログインから注文まで


import sys,os
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import chromedriver_binary

import codecs
import unittest
import string


# chromeを起動させる
chrome_options = webdriver.ChromeOptions()

# ヘッドレスバージョンを利用するオプションコマンド

#chrome_options.add_argument("--headless")
#driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()

arr = [7203,7201]

for id in arr:
    driver.get("https://kabutan.jp/stock/?code=" + str(id)) 
    driver.implicitly_wait(5)
    jikasougaku = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]/table[2]/tbody/tr[7]/td")
    owarine = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]/table[1]/tbody/tr[4]/td[1]")
    percent = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/section/div[1]/div[2]/div[1]/div[2]/dl/dd[2]/span")
    print(jikasougaku.text)
    print(owarine.text)
    print(percent.text)





