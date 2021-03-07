from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions
from time import sleep
import sys
sys.path.append("/home/mihnhyuk/PycharmProjects/pythonProject1/webauto")
import login
import addfavsearch


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get(url = 'https://map.naver.com/v5/?c=14150748.0814652,4500799.5110796,19,0,0,0,dh')
driver.implicitly_wait(3)

def add_fav_inNavermap(addresses):

    for address in addresses:
        print('경기도 부천시 ' + address[0] + ' ' + address[2])
        addfavsearch.search('경기도 부천시 ' + address[0] + ' ' + address[2], driver)
        addfavsearch.addfav(driver)
        sleep(1)
    addfavsearch.addfav(driver)

    sleep(10)
    #driver.close()