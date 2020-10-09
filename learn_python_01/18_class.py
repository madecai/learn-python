class Person :

	# 定义属性并给个默认值
	name = 'zhangsan'

	def hello(self) : 
		print('方法，和函数的区别就是，方法在调用的时候会默认传递一个参数，所以必须写一个形参接收，否则报错')
		print(self) # <__main__.Person object at 0x000001C28A7B54F0>

p1 = Person() # 实例化
p1.hello() # 会默认传递一个参数，就是当前的实例
print(type(p1)) # <class '__main__.Person'>

print('访问默认值', p1.name) # zhangsan
p1.name = 'lisi'
print('修改默认值', p1.name) # lisi
del p1.name
print('删除默认值', p1.name) # zhangsan

print('=========================================================属性不需要默认值，实例化时传递')
class Person :

	# 实例化时调用
	def __init__(self, age, sex) :
		self.age = age
		self.sex = sex


p2 = Person(11, 'male') # 此时调用 __init__
print(p2.age, p2.sex) # 11 male

p2.__init__(22, 'female') # 不要这么做
print('不要这么做', p2.age, p2.sex)

print('=========================================================隐藏属性，双下划线开头，只能在类内部使用，无法通过对象访问')
class Person :

	def __init__(self, name) :
		self.__name = name

	def get_name(self) :
		return self.__name

	def set_name(self) :
		return self.__name

p3 = Person('xxx')
print('p3.__name 在外部调用会报错') # AttributeError: 'Person' object has no attribute '__name'
print(p3.get_name()) # xxx
print('实际上是将名字修改为了：_类名__属性名 比如 __name -> _Person__name')
print('实际上仍然可以在外部访问，但不推荐这样做', p3._Person__name)

print('=========================================================使用装饰器使方法变得像属性一样调用')
class Person : 
	def __init__(self, name) :
		self._name = name

	@property
	def name(self) :
		return self._name

	@name.setter
	def name(self, name) :
		self._name = name

p4 = Person('aaa')
print('可以像属性一样访问', p4.name)
p4.name = 'bbb'
print('可以像属性一样修改', p4.name)