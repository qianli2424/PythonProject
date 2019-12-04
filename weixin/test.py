#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：
from weixin.openxls import OperExcel

op = OperExcel('test.xlsx','Sheet1')
data = ['正确的用例','用户名正确，密码正确','输入用户名和密码再提交','登录成功']
dict = {'name':'千里','sex':'男','age':'18'}
list = op.rdall()
print(list)