from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import requests
import time


##### UI #####
User = str(input("Please Input Account : "))
PW = str(input("Please Input Password : "))
Size = str(input("Please Input Size : "))
URL = str(input("Please Input Buy URL Link: "))
##### UI #####


##### Setup #####
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
##### Setup #####


##### Login #####
driver.get("https://www.nike.com/tw/")
time.sleep(5)
elements = driver.find_elements(By.TAG_NAME, "div")
print(elements)
for e in elements:
    print(e.text)
    if "登入" in e.text:
        print( "Didn't Login !!")
        element = driver.find_element("xpath",'//*[@id="gen-nav-commerce-header-v2"]/div[3]/div[1]/div/div/div[3]/div/button')
        time.sleep(5)
        element.click()
        time.sleep(5)
        element = driver.find_element("xpath",'/html/body/div[4]/div/div[1]/div/div[6]/form/div[2]/input')
        element.send_keys(User)
        element = driver.find_element("xpath",'/html/body/div[4]/div/div[1]/div/div[6]/form/div[3]/input')
        element.send_keys(PW)
        time.sleep(5)
        element = driver.find_element("xpath",'/html/body/div[4]/div/div[1]/div/div[6]/form/div[6]/input')
        element.click()
        time.sleep(5)
##### Login #####

##### Buy #####
# driver.get("https://www.nike.com/tw/launch/t/air-jordan-5-burgundy")
# driver.get("https://www.nike.com/tw/launch/t/kobe-8-protro-halo")
driver.get(URL)
time.sleep(5)
# driver.maximize_window()
# time.sleep(10)

class Getoutofloop(Exception):
    pass

try:
    while True:
        elements = driver.find_elements(By.TAG_NAME, "div")
        print(elements)
        for e in elements:
            print(e.text)
            if "購買 " in e.text:
                print("yes")
                raise Getoutofloop()
        driver.refresh()
        time.sleep(5)
except Getoutofloop:
    pass


# element = driver.find_elements(By.CLASS_NAME,"size-grid-dropdown size-grid-button")
elements = driver.find_elements(By.TAG_NAME, "li")
# element.click()
for e in elements:
    print(e.text)
    if e.text == "CM " + str(Size):
        driver.execute_script("arguments[0].scrollIntoView();",e)
        e.click()
        #　ActionChains(driver).move_to_element(e).click(e).perform()
        break
    # /html/body/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/section/div[2]/aside/div/div[2]/div/div[2]/div/button
e = driver.find_element("xpath",'/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button')
driver.execute_script("arguments[0].scrollIntoView();",e)
e.click()
#ActionChains(driver).move_to_element(e).click(e).perform()
time.sleep(5)
# driver.quit()
##### Buy #####