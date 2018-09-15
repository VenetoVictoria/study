#！/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yi"

info = {}

name = input("pls enter your name:")
age = int(input("pls enter your age:"))

info["name"] = name
info["age"] = age
#
# for i in info.items():
#     print(i)
# print('finish!!!')

for k,v in info.items():
    print("%s---->%s" %(k,v))





