d = {'a': 1, 'b': 2, 'c': 3}

#对于字典的迭代 默认迭代的是key，如果迭代value或者是key和value的话看下边的示例
for x in d:
	print(x)

#迭代字典的value，用到values()函数
for x in d.values():
	print(x)

#迭代字典的key和value
for x in d.items():
	print(x)

