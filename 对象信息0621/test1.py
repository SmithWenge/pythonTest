#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

import types

def fn():
	pass

# 判断一个对象是否是函数
print(type(fn) == types.FunctionType)
# 判断一个对象是否是int
print(type(123) == int)
# 判断一个对象是否是字符串
print(type('abc') == str)

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Husky(Dog):

    def run(self):
        print('Husky is running...')
	
a = Animal()
d = Dog()
h = Husky()

# 判断一个对象是否是某种类型
print(isinstance(a, Animal))
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
print(isinstance(h, Dog))
print(isinstance(h, Animal))

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 能用type()判断的基本类型也可以用isinstance()判断：

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个对象的所有属性和方法：
print(dir(a))
print(dir('abc'))