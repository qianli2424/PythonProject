#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：
from time import sleep

from selenium import webdriver

class Fslogin:
    def __init__(self):
        self.__d = webdriver.Chrome()
        self.__d.get('http://localhost/fsmarket/admin/')
        self.__username = self.__d.find_element_by_name('username')
        self.__password = self.__d.find_element_by_name('password')
        self.__loginButton = self.__d.find_element_by_css_selector('input.button2')
    def login(self,username,password):
        self.__username.send_keys(username)
        self.__password.send_keys(password)
        self.__loginButton.click()
    def __del__(self):
        sleep(3)
        self.__d.quit()