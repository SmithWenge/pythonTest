#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge


# 其中：
# a,b 为必选参数
# c=0 为默认参数
# *args 为可变参数，可变参数允许你传入 0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# **kw 为关键字参数，关键字参数允许你传入 0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def f1(a,b,c=0,*args,**kw):  
    print(a,b,c,args,kw)  
  
#在 python 中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数 5种参数形式。
#这 5 种参数都可以组合起来使用，但是注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。  

f1(1,2)  
f1(1,2,c=4)  
f1(1,3,6,'aw','wad',x=123,y='1232')  