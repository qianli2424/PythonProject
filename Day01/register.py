# !/usr/bin/python3
# @Author:千里
import xlrd


class Register:
    filePath = 'D:\\reg.xls'
    def __init__(self,username,password,comfirm):
        self.username = username
        self.password = password
        self.comfirm = comfirm
    def reg(self):
        name = self.readxls()
        if self.username not in name and self.password==self.comfirm:
            #print('注册成功,还要写数据')
            return {"errcode":"0","errmsg":"ok"}
        elif self.username in name:
            return {"errcode":"1","errmsg":"用户名已存在"}
            #print('用户名已存在')
        elif self.password != self.comfirm:
            return {"errcode": "2", "errmsg": "两次密码不一致"}
            #print('两次密码不一致')
        else:
            print('注册失败')
    #读文件的目的是为了验证用户名是否存在
    def readxls(self):
        excel = xlrd.open_workbook(self.filePath)
        sheet = excel.sheet_by_name('Sheet1')
        name = sheet.col_values(1,1)
        return name

