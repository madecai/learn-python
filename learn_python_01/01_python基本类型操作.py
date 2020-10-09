print('==========python中所有整形都是int，无最大长度')
a = 1231231231231231231232
print(a)
print('==========整形过长，可以下划线分隔，输出：123123123')
b = 123_123_123
print(b)
print('==========除法')
print(5 / 2) # 2.5
print(10 / 3) # 3.3333333333333335
print(6 / 2) # 3.5
print('==========除法取整')
print(10 // 3) # 3
print('==========幂运算，输出：121')
print(11 ** 2)
print('==========平方根，输出：4.0')
print(16 ** 0.5)
print('==========倒数，输出：0.04')
print(5 ** -2)
print('==========二进制0b开头，输出：2')
print(0b10)
print('==========八进制0o开头，输出：15')
print(0o17)
print('==========十六进制0x开头，输出：31')
print(0x1f)

print('==========python中所有的小数都是浮点型，浮点型可能得出不精确结果，输出：0.30000000000000004')
print(0.1 + 0.2)

print('==========字符串，python中如果代码过长，可以使用斜线换行，下面a输出结果不会换行')
a = '锄禾日当午，\
汗滴禾下土'
print(\
	a)
print('==========三引号，可以换行使用，保留格式（换行符）')
a = '''锄禾日当午，
汗滴禾下土'''
print(a)
print('==========打印Unicode码')
print('\u16a1')
print('==========python中字符串不能和其他类型运算')
print('==========print("a=" + 123) ==========会报错')
print('==========占位符')
print('hello %s'%'xiaoming')
print('hello %s %s'%('xiaoming', 'xiaohong'))
print('==========不够左边补空格，够了原封输出，输出： x')
print('hello %3s'%'x') 
print('==========整数也行，%s是万能的')
print('hello %3s'%123213) 
print('==========3到5之间多了截取，少了补齐，输出：xiaom')
print('hello %3.5s'%'xiaoming') 
print('==========保留两位小数，5也会舍弃，6才会入？精度不准，输出：123.33')
print('hello %.2f'%123.335000)
print('==========使用变量')
print('hello %s'%a)
print('==========直接嵌入变量')
a = 1
b = 2
print(f'hello {a}---{b}')
print('==========字符串复制，输出10次你好')
print('你好' * 10)
print('==========使用原始字符（不转义）', r'\r\n')

print('==========布尔值，相当于整型，可以和整型运算，True为1，False为0')
a = True
print(a)
print(a + 1)
a = False
print(a + 1)
print('==========空值')
b = None
print(b)
