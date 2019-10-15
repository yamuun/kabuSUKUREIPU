import sys
import codecs
import os
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import json
import chromedriver_binary
from datetime import date
import codecs
import unittest
import string




def removePlusMinus(str):
  #print(str.replace('+', ''))
  return str.replace('+', '')

def removeOKUEN(str):
  return str.replace(' 億円', '')



options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

arr = [7203,7201]

datastart = "[ "
dataend = " ]"

foradddata = datastart
for id in arr:
    driver.get("https://kabutan.jp/stock/?code=" + str(id)) 
    driver.implicitly_wait(5)
    companyName = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[3]/div[4]/h3")
    syoukenNO =  driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/section/div[1]/div[2]/div[1]/div[1]/h2/span")
    jikasougaku = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]/table[2]/tbody/tr[7]/td")
    owarine = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]/table[1]/tbody/tr[4]/td[1]")
    percent = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/section/div[1]/div[2]/div[1]/div[2]/dl/dd[2]/span")
    print(companyName.text)
    print(syoukenNO.text)
    print(removeOKUEN(jikasougaku.text))
    print(owarine.text)
    print(removePlusMinus(percent.text))

    targetstr = "{ \"syoukenNumber\" : " + syoukenNO.text + \
      ", \"companyName\" : " +"\"" + str(companyName.text) + "\"" \
      ", \"price\" : " + owarine.text + \
      ", \"jikasogaku\" : "  + removeOKUEN(jikasougaku.text) + \
      ", \"changePercent\" : " + removePlusMinus(percent.text) + \
      ", \"dateTime\" : " +"\"" + str(date.today()) +"\"" + " } "
    print(targetstr)

    foradddata = foradddata + targetstr + ","

foradddata = foradddata[:-1]
foradddata = foradddata + dataend

print(foradddata)

driver.quit()



headers = {
    'accept': 'text/plain',
    'Content-Type': 'application/json-patch+json',
}

#data = '[ { "syoukenNumber": 0, "companyName": "string", "price": 0, "jikasogaku": 0, "changePercent": 0, "dateTime": "2019-10-15T12:18:19.543Z" }]'
data = str(foradddata)
response = requests.post('http://localhost:60282/api/Kabuka/registList', headers=headers, data=data)

print(response)









