print('=======================open()的mode关键字参数')
# r 只读(默认就是r)，文件不存在报错
# w 可写，文件不存在则会创建，存在则会清空所有内容
# a 追加，文件不存在新建，文件存在追加内容
# x 用于新建文件，可读可写，文件不存在新建，文件存在报错，
# + 为操作符增加功能
# 	r+ 即可读又可写，文件不存在报错
# 	w+
# 	a+
file_name = './file_test/test_x_01.txt'
with open(file_name, 'x', encoding='utf-8') as file_obj:
	file_obj.write('aaa\n')
	file_obj.write(str(123) + '456\n')
	r = file_obj.write('你好')
	print('write返回写入的字符个数：', r) # 2

# 读取模式
# t 读取文本文件（默认值）
# b 读取二进制文件
# 读取文本文件时，size是以字符为单位的
# 读取二进制文件时，size是以字节为单位
file_name = './file_test/测试图片2.jpg'
with open(file_name, 'rb') as file_obj:
	new_name = './file_test/output/测试图片2输出.jpg'
	with open(new_name, 'wb') as new_file_obj:
		chunk = 1024 * 100
		while True:
			content = file_obj.read(chunk)
			print(content)
			if not content:
				break
			new_file_obj.write(content)
