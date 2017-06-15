#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 10:11:33
# @Author  : Sullivan (1980849329@qq.com)
# @Link    : https://github.com/SmithWenge


#质数的计算方式
noprimes = []

for i in range(2, 8):
	for j in range(i*2, 50, i):
		noprimes.append(j)

primes = []
for x in range(2, 50):
	if x not in noprimes:
		primes.append(x)

print(primes)