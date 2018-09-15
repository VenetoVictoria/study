#！/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yi"

import getpass

u=input("user:")
# p=input("password:")
p=input("password:")

num = 0
while True:
    if u == "tom" and p == "123":
        print("登陆成功！")
        break
    else:
        num +=1
        print("失败次数%s" %(num))
        if num == 3:
            print("登录失败！")
            break
        u=input("user:")
        p=input("password:")

# else:
#     print("x欢迎登陆！")
