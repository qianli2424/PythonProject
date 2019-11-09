# !/usr/bin/python3
# @Author:千里
import unittest
from Day01 import testcase


class Test:
    suit = unittest.TestSuite() #创建一个袋子放用例的
    case = ''
    load = unittest.TestLoader()    #用来放用例而做准备
    case = suit.addTest(load.loadTestsFromTestCase(testcase.TestCase))

    #为执行而生
    runner = unittest.TextTestRunner()
    runner.run(suit)
