print('======================================================可以使用help(函数查看python中的函数用法')
help(print)

print('======================================================文档字符串')
def test01(a:int, b:bool, c:str='hello') :
	'''
	文档字符串示例
	函数的作用。。。
	函数的参数:
		a,作用，类型，默认值
		b,作用，类型，默认值
		c,作用，类型，默认值
	'''
	return 10

help(test01)