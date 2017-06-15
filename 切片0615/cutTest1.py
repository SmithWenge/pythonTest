#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

import os

l = []
n = 0;
while n < 10:
	l.append(n)
	n = 1 + n

print(l)

# r = []
# def output(y):
# 	for x in range(y):
# 		r.append(l[x])
# 	print(r)

# output(8)


#会输出索引0到8但是不包含最后一个
print(l[0:8])
print(l[1:8])
print(l[:8])
print(l[2:5])
print(l[1:5])
print(l[-1:-5])

#字符串也支持切片操作
#相对于java来说 python的切片操作就太简单了
print('abcdef'[2:4])
