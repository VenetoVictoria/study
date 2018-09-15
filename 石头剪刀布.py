#！/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yi"
#调用ranmdom模块
import random
#给列表l1赋值
l1 = ['石头','剪刀','布']
#给元组l2复制
l2 = ["石头","剪刀"],["剪刀","布"],["布","石头"]
#给用户提供的规则列表
prompt = """(0)石头
(1)剪刀
(2)布
请选择（0|1|2）："""

cw = 0
pw = 0
#三局两胜制，人和电脑胜利次数不满足2时继续循环。
while cw < 2 and pw <2:
    index = int(input(prompt))
    #当输入选项大于3时，继续循环输入
    while index >= 3:
        index = int(input(prompt))
    #通过输入的数字（脚标）来，调用输入的选项（石头|剪刀|布）
    player = l1[index]
    #调用模块实现随机选项（石头|剪刀|布）
    computer = random.choice(l1)
    #打印出人和电脑的出拳，方便比对
    print("player:%s,computer:%s" %(player,computer))
    #通过if语句来判断输赢
    if player == computer:
        print("\033[28;44;1m平局！\033[0m")
    #通过匹配出拳组合，是否存在于胜利的元组l2中来判断赢
    elif [player,computer] in l2:
        #print("\033[29;44;1m你赢了！\033[0m")
        pw +=1
        print("你赢了%s次" %pw)
    else:
        #print("\033[30;44;1m你输了！\033[0m")
        cw +=1
        print("你输了%s次" %cw)
#三局两胜制，通过输赢次数
if pw == 2:
    print("Win!")
else :
    print("Lose!")

