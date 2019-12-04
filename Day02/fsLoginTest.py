#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：
import unittest
from Day02.fslogin import Fslogin

class FsLoginTest(unittest.TestCase):
    def __init__(self,methodName,expected,data):
        self.expected = expected
        self.data = data
        super().__init__(methodName)

    def setUp(self) -> None:
        None
    def tearDown(self) -> None:
        None

    def test_login(self):
        #生成登录对象，执行doLogin方法的结果为实际结果result
        obj = Fslogin(*self.data)
        result = obj.doLogin()
        #断言：将实际结果与预期结果进行比较
        print('预期结果为：' + str(self.expected) + ',实际结果为：' + str(result))
        self.assertEqual(self.expected,result)