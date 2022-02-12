from selenium import webdriver
import time

browser = webdriver.Safari()
url = "https://www.miniclip.com/games/bubble-trouble/en/#privacy-settings"
browser.get(url)
browser.maximize_window()
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
