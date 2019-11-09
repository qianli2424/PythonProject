#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：添加测试，执行测试
import unittest
from HTMLTestReport import HTMLTestRunner
from unittestDemo.LoginTest import LoginTest

#通过列表的方式编写测试用例，测试用例中主要包括测试数据和预期结果
case = [{'data':('admin','123456'),'expected':{'code':200,'msg':'登录成功'}},
        {'data':('root','123456'),'expected':{'code':500,'msg':'用户名或密码错误'}},
        {'data':('admin','111111'),'expected':{'code':500,'msg':'用户名或密码错误'}},
        {'data':('','123456'),'expected':{'code':404,'msg':'用户名或密码不能为空'}},
        {'data':('admin'),'expected':{'code':404,'msg':'用户名或密码不能为空'}}]

#构造测试集，并在测试集中添加测试用例，通过for循环可以依次读取所有的测试数据
suite = unittest.TestSuite()
for i in case:
    suite.addTest(LoginTest('test_login',i['expected'],i['data']))

#创建一个TextTestRunner对象并执行测试集（所有的测试用例）
with open('report.html','wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='测试报告',
        description='登录单元测试报告',
        tester='千里'
    )
    #所有的测试用例都被装载进了suite套件中，只需要执行suite对象便可完成全部用例的测试
    runner.run(suite)