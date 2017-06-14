#命名关键字参数
# *后面的参数被视为命名关键字参数。
def persion(name, age, *, city, job):
	print(name, age, city, job)

def persion2(name, age, city, job):
	print(name, age, city, job)


persion('wenge', 18, job='progremer', city='beijing')
persion2("wenge", 18, "beijing", "progremmer")
persion2("wenge", 18, job="progremmer", city="beijing")