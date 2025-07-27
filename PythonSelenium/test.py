from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service("./chromedriver"))
driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
time.sleep(1)

radio = driver.find_element(By.CSS_SELECTOR, "input[value='rd1']")
radio.click()
time.sleep(1)