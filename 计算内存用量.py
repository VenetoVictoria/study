#！/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yi"
#取内存总量
f = open("/proc/meminfo","r")

for lines in f:
	# 在/proc/meminfo中匹配到"MemTotal:"这一行
    if lines.startswith("MemTotal:"):
    	#打印出以" "为分割符，角标为1的一项
        memtotal = int(lines.split()[1])/1024/1024
    # 在/proc/meminfo中匹配到"MemFree:"这一行
    if lines.startswith("MemFree:"):
    	#打印出以" "为分割符，角标为1的一项
        memfree = int(lines.split()[1])/1024/1024
        break
print("Used:%.2fG -%.2fG = %.2fG" %(memtotal,memfree,memtotal-memfree))
