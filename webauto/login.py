from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions
import pyperclip

def log_in(driver, User_ID, User_PW):
    try:
        login = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gnb_login_button')))
        login.click()

        ID_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'id')))
        PW_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pw')))

        pyperclip.copy(User_ID)
        ID_box.send_keys(Keys.CONTROL, 'v')
        pyperclip.copy(User_PW)
        PW_box.send_keys(Keys.CONTROL, 'v')

        login_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="log.login"]')))
        login_btn.click()
    except :
        print("log_in error!")
        exit()
