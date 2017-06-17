#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，
# 所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。


def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 把一个序列中的空字符串删掉
# strip()函数是去除特定的字符，默认是空字符串
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))