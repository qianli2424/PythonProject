#!/usr/bin/python3
#-*- coding=utf8 -*-
#文件说明：登录功能
def login(self,username,password):
    if username=='admin' and password=='123456':
        return {'code':200,'msg':'登录成功'}
    elif username!='admin' or password!='123456':
        return {'code':500,'msg':'用户名或密码错误'}
    elif username=='' or password=='':
        return {'code':404,'msg':'用户名或密码不能为空'}