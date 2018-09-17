#!/usr/bin/env python
#==== coding:utf-8 ====
__author__ = "Yi"

cd="""caidan:
0.kele
1.xuebi
2.shupian
3.break
qingxuanze(0|1|2|3):"""

index=int(input(cd))

while index >=4:
    index = int(input(cd))


if index == 0:
    print("kele:3yuan")
elif index == 1:
    print("xuebi:4yuan")
elif index == 2:
    print("shupian:5yuan")
elif index == 3:
    print("tuichu")