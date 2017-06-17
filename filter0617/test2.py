#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

#用filter求素数(埃氏筛法)

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#对it序列里的每一个元素进行判断。
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break