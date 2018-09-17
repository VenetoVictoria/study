#!/usr/bin/env python
#==== coding:utf-8 ====
__author__ = "Yi"


def cp(x,y):
    x1=open(x)
    y1=open(y,'w')

    while True:
        data=x1.read()
        if not data:
            break
        y1.write(data)

    x1.close()
    y1.close()

cp("/123.py","/123.sh")