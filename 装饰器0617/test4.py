#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge
import functools

def log(param):
    if hasattr(param,'__call__'):
        @functools.wraps(param)
        def warpper(*args, **kw):
            print('begin call')
            _rsFunc = param(*args, **kw)
            print('after call')
            return _rsFunc
        return warpper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin else call')
                print(param)
                _rsFunc = func(*args, **kw)
                print('after else call')
                return _rsFunc
            return wrapper
        return decorator

@log
def now():
    print('2015-3-25')

now()