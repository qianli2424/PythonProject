#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：登录的测试用例
import unittest
from unittestDemo.Login import Login

class LoginTest(unittest.TestCase):
    def __init__(self,methodName,expected,data):
        self.expected = expected
        self.data = data
        super().__init__(methodName)

    def setUp(self) -> None:
        None
    def tearDown(self) -> None:
        None
    #简化后的测试用例只需要编写一个test_login方法即可
    def test_login(self):
        #生成登录对象，执行doLogin方法的结果为实际结果result
        obj = Login(*self.data)
        result = obj.doLogin()
        #断言：将实际结果与预期结果进行比较
        print('预期结果为：' + str(self.expected) + ',实际结果为：' + str(result))
        self.assertEqual(self.expected,result)
        # try:
        #     self.assertEqual(self.expected,result)
        # except BaseException as e:
        #     print('用例执行未通过')
        #     print('预期结果为：' + str(self.expected) + ',实际结果为：' + str(result))
        #     testResult = '不通过'
        #     raise testResult
        # else:
        #     print('用例执行通过')
        #     print('预期结果为：' + str(self.expected) + ',实际结果为：' + str(result))
        #     testResult = '通过'