#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：登录功能
class Login:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def doLogin(self):
        if self.username=='admin' and self.password=='123456':
            return {'code':200,'msg':'登录成功'}
        elif self.username!='admin' or self.password!='123456':
            return {'code':500,'msg':'用户名或密码错误'}
        elif self.username=='' or self.password=='':
            return {'code':404,'msg':'用户名或密码不能为空'}