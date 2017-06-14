def add(x,y):
	print(x + y)

#可变参数
def adds(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)

#关键字参数
def person(name, age, **wenge):
    print('name:', name, 'age:', age, 'other:', wenge)


add(4,5)
adds(1,2,3,4)

nums = [1,2,3,4]
adds(*nums)
adds(*[1,2,3,4])

person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)