#！/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yi"


l1 = [0,1]
p =int(input("please your sumber:"))

for i in range(p-2):
    l1.append(l1[-1]+l1[-2])
print(l1)
