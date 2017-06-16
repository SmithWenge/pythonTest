#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

# 特性2 函数名也是变量
abs = 10
#print(abs(-10))
# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

# 要让修改abs变量的指向在其它模块也生效，要用import test2; test2.abs = 10。