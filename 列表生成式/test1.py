#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

import os

#先来个最简单的要生成数字的list
l = list(range(1, 11))
print(l)
#list转成tuple
print(tuple(l))

#遍历的过程中直接计算
l2 = [x * x for x in range(1, 11)]
print(l2)

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l3)

#还可以使用两层循环，可以生成全排列：
l4 = [m + n for m in 'ABC' for n in 'XYZ']
print(l4)

#列出当前目录下的所有文件和目录名，可以通过一行代码实现：
l5 = [d for d in os.listdir('..')] # os.listdir可以列出文件和目录
print(l5)

#大小写也可以直接在循环中搞定
l6 = ['Hello', 'World', 'IBM', 'Apple']
l7 = [s.lower() for s in l6]
print(l7)

