class A(object) :
	# 类属性
	count = 0

	def __init__(self, name) :
		# 实例属性
		self.name = name

	def test_01(self) :
		print('实例方法')

	@classmethod
	def test_02(cls) :
		print('类方法，可以通过类调用，也可以通过实例调用，会默认传递一个cls：', cls)
		print(cls.count)

	@staticmethod
	def test_03() :
		print('静态方法，无需设置参数，就相当于定义在类中的函数')

a = A('hhh')
print('============== a.count, A.count等价的', a.count, A.count)
print('============== A.name不能访问，只能使用a.name', a.name)
print('============== a.test_01() 等价于 A.test_01(a)')
a.test_01()
A.test_01(a)
print('============== a.test_02() 等价于 A.test_02()')
a.test_02()
A.test_02()
print('============== a.test_03() 等价于 A.test_03()')
a.test_03()
A.test_03()