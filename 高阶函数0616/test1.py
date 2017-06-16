#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

# 特性1 变量可以指向函数
f = abs
print(f(-10))# 求绝对值
print(abs(-10))

#说明变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。