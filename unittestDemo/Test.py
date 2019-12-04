#!/usr/bin/python3
# -*- coding=utf8 -*-
# 文件说明：装载测试用例，运行测试
import unittest
from HTMLTestReport import HTMLTestRunner
from unittestDemo import LoginTest

#创建一个用例集合用来装载测试用例
suite = unittest.TestSuite()
#*****装载测试用例，使用TestLoader方法装载用例********
loader = unittest.TestLoader()
#LoginTest为测试模块LoginTest.py，一个py文件就是一个模块，文件名就是模块名
suite.addTest(loader.loadTestsFromModule(LoginTest))

#创建一个TextTestRunner对象并执行测试集（所有的测试用例）
with open('report.html','wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='测试报告',
        description='登录单元测试报告',
        tester='千里'
    )
    runner.run(suite)