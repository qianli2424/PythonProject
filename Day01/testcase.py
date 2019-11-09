# !/usr/bin/python3
# @Author:千里
import unittest
import xlrd
from Day01.register import Register

class TestCase(unittest.TestCase):
    def setUp(self):
        print('无前置步骤')
    def tearDown(self):
        print('无后置步骤')
    def testReg(self):
        #操作的是哪个excel
        excel = xlrd.open_workbook("D:\\case.xls")
        #操作的是哪个sheet页，第0个
        sheet = excel.sheet_by_index(0)
        #有多少行数据
        rows = sheet.nrows
        for index in range(rows):
            #取得一行数据，这里是取最后一行
            case = sheet.row_values(rows-1)
            #只是产生了一个Register类的对象
            regUser = Register(case[1], case[2], case[3])
            result = regUser.reg()   #才真正意义上完成的是注册操作

            #实际结果与预期结果的比较
            try:
                self.assertEqual(result, case[4])
            except AssertionError as a:
                raise a
            else:
                print("用例执行通过，账户已存在")



