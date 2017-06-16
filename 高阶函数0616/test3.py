#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

# 传入函数作为参数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))

# 完事想了想这么做的意义，为什么不直接调用函数而非要把函数作为参数呢？只想到了这样做更加灵活，别的还没有想到。留一个flag。