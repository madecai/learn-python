print('==========类型检查')
print(type(123)) # <class 'int'>
print(type('123')) # <class 'str'>
print(type(1.5)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'>

print('==========类型转换')
print('bool转整型',int(True))
print('str转整型',int('123'))
print('str转整型，格式不对会报错>>int("11.5")')
print('float转整型',int(1.5))
print('None转整型会报错>>int(None)')

print('int转浮点型，输出6.0----',float(6))
print('bool转浮点型，输出0.0----',float(False))

print('int转字符串', str(6))
print('None转字符串，输出名为None的字符串', str(None))

print('None转布尔, 输出False>>', bool(None))
print('空字符串转布尔, 输出False>>', bool(''))
print('空白字符串转布尔, 输出True>>', bool(' '))