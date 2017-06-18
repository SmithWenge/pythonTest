#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

# 在Python中，定义类是通过class关键字
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的

class Student(object):
    pass

stu = Student()
# 可以自由地给一个实例变量绑定属性，比如，给实例stu绑定一个name属性,不用在类中定义
stu.name = 'wenge'
print(stu)
print(stu.name)

class Student2(object):

	#__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
	# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
	# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
    def __init__(self, name, score):
        self.name = name
        self.score = score

stu2 = Student2('wenge', 22)
print(stu2.name, stu2.score)

# 可以通过函数来访问对象的这些数据
def print_score(st):
	print('%s: %s' % (st.name, st.score))

print_score(stu2)