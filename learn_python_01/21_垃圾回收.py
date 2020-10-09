class A:
	def __init__(self) :
		self.name = 'xxx'

	def __del__(self) :
		print('__del__在垃圾回收前调用')

a = A()

# a = None
# del a

input('回车退出')
