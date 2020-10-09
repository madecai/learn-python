print('====================================================定义装饰器')
def add(a ,b) : 
	print('执行a+b')
	return a + b

def begin_end(old) :
	'''
		装饰器对函数进行扩展
		参数:
			old 要扩展的参数
	'''
	# 定义一个不定长元组参数，接收所有位置参数
	# 定义一个不定长字典参数，接收所有关键字参数
	def new_func(*args, **kwargs) :
		print('执行开始') 
		result = old(*args, **kwargs)
		print('执行结束') 
		return result
	return new_func

wrap = begin_end(add)
print(wrap(1, 2))

print('====================================================快速装饰一个方法')
@begin_end # 如果有多个先包装最下面的
def hello() :
	print('hello')
hello()