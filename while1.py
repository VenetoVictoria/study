#！/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yi"

x = ""
pro="""请选择内容：
1.肥宅快乐水
2.肥宅快乐茶
3.肥宅快乐事
请选择（1|2|3）："""


while not x:
    # print("请选择内容：")

    x= int(input(pro))
    while x>3:
        x=int(input(pro))
    if x == 1:
        print("20元")
    elif x == 2:
        print("50元")
    elif x == 3:
        print("100元")
    # else:
    #     print("请支付！")









