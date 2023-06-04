import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds

url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"

driver.get(url)

elements = driver.find_elements(By.CSS_SELECTOR, ".primary")

for elt in elements:
    print(elt.text)

driver.quit()
