#!/usr/bin/env python
#==== coding:utf-8 ====
__author__ = "Yi"


import  sys,random,string

def password(x):
    pwd = " "
    #chuang jian bian liang  zhi wei a-zA-Z0-9
    all=string.ascii_letters + string.digits
    for i in range(x):
        #da yin sui ji su bin pin jie
        pwd += random.choice(all)
    print(pwd)

if __name__ == '__main__':
    for i in range(int(sys.argv[2])):
        password(int(sys.argv[1]))