from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
for i in range(10):

        def spambot() :
                driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
                driver.get("https://www.instagram.com/")
                actions = ActionChains(driver)
                sleep(4)
                driver.find_element_by_name("username").send_keys("lalitha6159")
                driver.find_element_by_name("password").send_keys('lalitha@6159')
                driver.find_element_by_xpath("//button[@type='submit']").click()
                sleep(5)
                driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
                sleep(3)
                driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
                driver.maximize_window()
                driver.find_element_by_xpath("//a[contains(@href,'/direct/inbox')]").click()
                sleep(2)
                driver.find_element_by_xpath("//a[contains(@href,'/direct/t/340282366841710300949128116552743537342')]").click()
                sleep(2)
                actions.send_keys("YAM SEND DIS VIA AUTO BOT")
                actions.perform()
                sleep(1)
                driver.find_element_by_xpath("//button[contains(text(),'Send')]").click()
                sleep(2)
                driver.back()
                sleep(1)
                driver.back()
                sleep(1)
                driver.close()

for i in range(10):
        spambot()

