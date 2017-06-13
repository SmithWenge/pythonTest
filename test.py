def add(x,y):
	print(x + y)

def adds(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

add(4,5)
adds(1,2,3,4)

nums = [1,2,3,4]
adds(*nums)
adds(*[1,2,3,4])

person('Adam', 45, gender='M', job='Engineer')