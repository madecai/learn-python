print('========================特殊方法，也称魔术方法，以__开始和结尾的')
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# 尝试对象转称字符串时调用
	def __str__(self):
		return 'Person [name = %s, age = %d]'%(self.name, self.age)

	# 对当前对象使用repr()方法时调用
	def __repr__(self):
		return 'Hello'

	# 转成bool时调用
	def __bool__(self):
		return self.age > 17

	# 对对象做大于比较时调用
	def __gt__(self, other):
		return  self.age > other.age

	# 添加一个len
	def __len__(self):
		return 11

p = Person('zhangsan', 20)
print('打印p：', p) # Person [name = zhangsan, age = 20]

print('调用repr', repr(p))

p2 = Person('lisi', 10)
print('p的年龄比p2大', p > p2)

if p :
	print('p成年了')
else :
	print('p未成年')

print('本来调用len会报错，但是加上__len__的魔术方法后就走魔术方法了：', len(p))

print('可以使用中括号访问')
class Person: 
	def __getitem__(self, item): 
		print(item)
		return self.info[item]

p = Person()
p.info = {'name': 'a', 'age': 11}
print(p['name'])

print('object中有如下魔术方法可覆盖')
 # object.__add__(self, other)
 # object.__sub__(self, other)
 # object.__mul__(self, other)
 # object.__matmul__(self, other)
 # object.__truediv__(self, other)
 # object.__floordiv__(self, other)
 # object.__mod__(self, other)
 # object.__divmod__(self, other)
 # object.__pow__(self, other[, modulo])
 # object.__lshift__(self, other)
 # object.__rshift__(self, other)
 # object.__and__(self, other)
 # object.__xor__(self, other)
 # object.__or__(self, other)
 # object.__lt__(self, other) 小于 <
 # object.__le__(self, other) 小于等于 <=
 # object.__eq__(self, other) 等于 ==
 # object.__ne__(self, other) 不等于 !=
 # object.__gt__(self, other) 大于 >
 # object.__ge__(self, other) 大于等于 >= 
