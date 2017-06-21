#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

# 可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)

# 给实例绑定name属性
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# 但是类属性并未消失，用Student.name仍然可以访问
s.name = 'Michael'
print(s.name)
print(Student.name)

# 删除实例的name属性，只是实例的属性
del s.name
print(s.name)
print(Student.name)