#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：登录的测试用例
import unittest
from ddt import ddt, data, unpack
from unittestDemo.Login import login

data = [['admin','123456','success'],['admin','111111','404']]

class LoginTest(unittest.TestCase):
    @ddt
    def setUp(self) -> None:
        None
    @data(*data)
    @unpack
    def tearDown(self) -> None:
        None
    #简化后的测试用例只需要编写一个test_login方法即可
    def test_login(self):
        #生成登录对象，执行login方法的结果为实际结果result
        result = login(*self.data)
        #断言：将实际结果与预期结果进行比较
        print('预期结果为：' + str(self.expected) + ',实际结果为：' + str(result))
        self.assertEqual(self.expected,result)