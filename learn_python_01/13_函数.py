print('==========================================1、使用位置参数，就是第一个实参赋值给第一个形参，第二个。。。')
def test01(a, b = 1) :
	return f'a={a} and b={b}'
print(test01(1, 2)) # 3
print('使用默认值', test01(1)) # 2
print('执行test01()参数不一致，报错') # TypeError: test01() missing 1 required positional argument: 'a'
print('==========================================2、使用关键字参数，不用按照顺序')
print('使用关键字参数', test01(b = 2, a = 3))
print('混合使用时，关键字参数写后面', test01(1, b = 3))
print('==========================================3、不定长参数（装包）')
def sum(*nums) : 
	print('接收到的类型是一个元组', type(nums)) # <class 'tuple'>
	result = 0
	for n in nums : 
		result += n
	return result
print(sum(1, 1, 2)) # 4

print('不定长参数只能有一个，无需放最后，不定长参数后必须使用关键字参数传递')
def test02(a, *b, c) : 
	print(f'a={a}, b={b}, c={c}')
test02(1, 2, 3, c = 4) # a=1, b=(2, 3), c=4

print('**只能有一个，且必须写在最后')
print('**接收其他的关键字参数，key就是关键字，value就是传的值')
def test03(a, b, **c) : 
	print(f'a={a}, b={b}, c={c}')
test03(1, 2, x = 3, c = 4) # a=1, b=2, c={'x': 3, 'c': 4}
print('==========================================4、不定长参数（拆包）')
print('元组拆包')
def test04(a, b, c) :
	print(f'a={a}, b={b}, c={c}')
t = (1, 2, 3)
test04(*t)
print('字典拆包')
d = {'a':10, 'b':20, 'c':30}
test04(**d)