print('===============================================================变量作用域')
a = 10 # 全局变量
def test01() :
	a = 20
test01()
print('不会改变全局变量的值', a) # 10

def test02() :
	global a # 使用global声明，后面使用的就是全局的a
	a = 20
test02()
print('会改变全局变量的值', a) # 20

print('===============================================================全局命名空间')
scope = locals() # 当前命名空间
print(type(scope)) # <class 'dict'>
print(scope)

scope['b'] = '全局变量'
print('添加一个全局变量，不建议这么做', b) # 全局变量

print('===============================================================函数中的命名空间')
def test03() :
	c = 'xxx'
	scope = locals()
	scope['d'] = 'dddd' # 不建议
	print(scope)
test03()
print('===============================================================任意地方获取全局的命名空间')
print(globals()) # 函数外部
def test04() :
	global_scope = globals()
	print(global_scope) # 函数内部
test04()