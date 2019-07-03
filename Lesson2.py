from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://localhost/phpwind")
driver.find_element_by_id("nav_pwuser").send_keys("admin")
driver.find_element_by_name("pwpwd").send_keys("123456")
driver.find_element_by_name("head_login").click()
sleep(5)
driver.find_element_by_link_text("默认版块").click()
sleep(5)
driver.close()