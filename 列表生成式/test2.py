#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge

import os

L1 = ['Hello','World',18,'Apple',None]
L2 = [x.lower() for x in L1 if isinstance(x,str)==True]
L3 = [s.lower() if isinstance(s,str) else s for s in L1]
L4 = [s.upper() if isinstance(s,str) is True else s for s in L3]
L5 = [s[:1].upper()+s[1:].lower() if isinstance(s,str) else s for s in L4]

print(L2)
print(L3)
print(L4)
print(L5)
