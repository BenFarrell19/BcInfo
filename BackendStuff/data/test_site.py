from selenium import webdriver
import csv
from time import sleep
from selenium.webdriver.common.by import By
import re


from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('C:/Users/benf7/Desktop/chromedriver.exe')
url = 'https://wcc.sc.egov.usda.gov/nwcc/yearcount?network=sntl&state=MT&counttype=statelist'

driver.get(url)
sleep(3)
lst = []
for i in range(2,96):

    elem = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[{}]/td[3]'.format(i))

    lst.append((re.sub(r'[^0-9]', '', elem.text)+":MT:SNTL"))

print(lst)

