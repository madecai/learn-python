print('=======写法1、import 模块名（就是python文件的名字，不包含扩展名）')
import test_module
print(test_module.a)
print('=======写法2、import 模块名 as 别名')
import test_module as test
print('拿到模块名：', test.__name__) # test_module
print('在主模块中打印__main__，直接通过python执行的模块就是主模块：', __name__) #  __main__
print('起别名以后就只能使用别名了，使用test_module报错', test.a)

print('使用模块中的变量：', test.a)

print('=======写法3、from 模块名 import 变量')
from test_module import a, _b
print('这种方式可以直接使用变量：', a)
print('这种方式可以直接使用变量：', _b)

print('=======写法4、from 模块名 import 变量 as 别名')
from test_module import c as test_02
print('起别名以后就只能使用别名了，使用c报错：', test_02) # NameError: name 'c' is not defined

print('=======写法5、from 模块名 import *')
from test_module import * # 一般不会使用
print('这种写法可以直接使用变量：', e)
print('这种方式不能使用下划线开头的属性：_f ') # NameError: name '_d' is not defined

print('=======写法6、使用包')
# __init__.py相当于class中的baidef __init__(self):函数，用来初始化模块
from hello import str_utils, date_utils
print(str_utils.name_1)
print(date_utils.name_2)
print('不能使用__init__.py中的方法test()', ) # TypeError: 'module' object is not callable

