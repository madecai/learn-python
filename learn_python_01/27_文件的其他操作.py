with open('file_test/test_01.txt', 'rt', encoding='utf-8') as file_obj:
	#   seek()需要两个参数
	#   第一个 是要切换到的位置
	#   第二个 计算位置方式
	#       可选值：
	#           0 从头计算，默认值
	#           1 从当前位置计算
	#           2 从最后位置开始计算
	file_obj.seek(5)
	print(file_obj.read())
	print('tell() 方法用来查看当前读取的位置：',file_obj.tell())

import os
from pprint import pprint
# os.listdir() 获取指定目录的目录结构，返回一个列表，接收一个参数，默认为. 即当前目录
print(os.listdir('file_test'))
print('获取当前文件所在目录：', os.getcwd()) # C:\Dev\workspace\python\learn_python_01
print('切换当前文件所在目录：', os.chdir('c:/')) # None
print('获取当前文件所在目录：', os.getcwd()) # c:\
print('删除目录：', os.rmdir('aaa')) # None
print('创建目录：', os.mkdir('aaa')) # None
print('新建文件，涉及权限用管理员运行', open('aa.txt','w')) # <_io.TextIOWrapper name='aa.txt' mode='w' encoding='cp65001'>
print('重命名或移动', os.rename('aa.txt', 'bb.txt')) # None
print('删除文件，文件不存在会报错：', os.remove('bb.txt')) # None

