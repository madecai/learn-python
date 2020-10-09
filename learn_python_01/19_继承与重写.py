print('=====================================================继承')
class Animal :
	def run(self) :
		print('动物会跑')

class Dog(Animal) : 
	def bark(self) :
		print('汪汪汪')

dog = Dog()
dog.bark()
dog.run()

print('=====================================================如果省略父类，默认父类为object')
class Person(object) :
    pass

p = Person()
print(isinstance(p, object)) # True
print(type(print)) # <class 'builtin_function_or_method'>
print(isinstance(print, object)) # True

print('=====================================================重写，（覆盖 override）')
class Pig(Animal) : 
	# 可以重写父类所有方法，包括装饰器方法和__init__
	# 可以使用super()方法获取父类，并且调用父类方法时，不需要传self
	def run(self) :
		super().run()
		print('猪跑的慢')

pig = Pig()
pig.run()
print('=====================================================多重继承，尽量避免使用')
class A :
	def test(self) :
		print('A类中的test')

class B :
	def test(self) :
		print('B类中的test')

class C(A, B) :
	pass

c = C()
c.test() # A类中的test
print('会优先取第一个，然后第二个。。。')

print('=====================================================多态')
def run(animal) : 
	animal.run()
run(Pig())
run(Dog())
