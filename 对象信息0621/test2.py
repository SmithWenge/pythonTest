#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

# 有属性'x'吗？
print(hasattr(obj, 'x')) 
print(obj.x)

# 有属性y吗
print(hasattr(obj, 'y'))
# 设置一个属性y
setattr(obj, 'y', 19)
#获取属性y
print(obj.y)
print(getattr(obj, 'y'))

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# print(getattr(obj, 'z'))

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 23))

# hasattr和getattr方法同样也适用于对象的方法
# 判断有没有属性power
print(hasattr(obj, 'power'))
# 或取到power方法然后赋值给参数fn
fn = getattr(obj, 'power')
print(fn)



# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息
# 对象的hasattr，getattr，setattr方法相当于java中反射的部分应用。