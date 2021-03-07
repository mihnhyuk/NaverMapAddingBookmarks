from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions

def search(address_bungee, driver):
    try:
        search_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//search-input-box//input')))
        search_box.clear()
        search_box.send_keys(address_bungee)
        search_box.send_keys(Keys.RETURN)

    except:
        print("can't find searchbox!")

def addfav(driver):
    try:
        fav_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-address/div/div[2]/div/div[1]/div[2]/div[2]/button[1]')))
        fav_btn_class = fav_btn.get_attribute('class')
        fav_btn_class_attribute = fav_btn_class.split()
        #print(fav_btn_class_attribute)

        if "active" not in fav_btn_class_attribute:
            #print('fav_btn is found')
            fav_btn.click()
            complete_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bookmark"]/div[1]/div[2]/button')))
            complete_btn_class = complete_btn.get_attribute('class').split()
            #print(complete_btn_class)
            complete_btn.send_keys(Keys.ENTER)

        else:
            print('already in fav!')


    except exceptions.NoSuchElementException:
        print("can't find btn!")
    except exceptions.TimeoutException:
        print("Timeout")


