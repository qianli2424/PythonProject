#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：
from selenium import webdriver

d = webdriver.Chrome()
d.get('https://www.baidu.com')
ele = d.find_elements_by_css_selector('#u1 > a')
print(len(ele))
for i in range(len(ele)):
    list =  d.find_elements_by_css_selector('#u1 > a')
    list[i].click()
    print(d.title)
    d.back()
d.close()