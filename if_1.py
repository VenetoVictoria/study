#！/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yi"

import getpass

user = input("please input your name:")
passwd = getpass.getpass("please input your password:")

if user == 'tom' and passwd == '123':
    print("login")
else:
    print("nologin")
