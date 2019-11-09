from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
inputs = driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute("type") == "checkbox":
        input.click()
sleep(5)
driver.close()