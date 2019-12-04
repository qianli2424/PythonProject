#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：
import openpyxl

data = ['正确的用例','用户名正确，密码正确','输入用户名和密码再提交','登录成功']
file = openpyxl.load_workbook('test.xlsx')
sheet = file['Sheet1']

file.close()