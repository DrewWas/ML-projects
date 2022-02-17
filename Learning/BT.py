from selenium import webdriver
from time import sleep
import pyautogui

#x coordinates - (57, 1856)
#y coordinates - (500, 1374)


def setup():
    driver = webdriver.Safari()
    url = "https://www.miniclip.com/games/bubble-trouble/en/#privacy-settings"
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath('//button[contains(text(), "OK")]').click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, 300)") 
    sleep(10)
    pyautogui.moveTo(400,400)
    pyautogui.click()
    print("click")
    sleep(50)


setup()

