#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

l1 = sorted([36, 5, -12, 9, -21])

print(l1)

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。注意输出的还是原始序列，而不是被key函数改变后的序列。
# 这里我们就应该体会出函数做参数也就是所谓的高阶函数的简洁之处
l2 = sorted([36, 5, -12, 9, -21], key=abs)

print(l2)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
l3 = sorted(['bob', 'about', 'Zoo', 'Credit'])

print(l3)

# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，
# 只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，
# 实际上就是先把字符串都变成大写（或者都变成小写），再比较。

# 这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
l4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

print(l4)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
l5 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

print(l5)


# 总结：
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。