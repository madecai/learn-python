print('==========元组是一个不可变的序列，相当于一个不可变的列表')
print('创建一个空元组')
my_tuple = ()
print(my_tuple) # ()
print(type(my_tuple)) # <class 'tuple'>
print('创建一个五个元素的元组')
my_tuple = (1,2,3,4,5)
print(my_tuple)
print('元组不为空时，括号可以省略')
my_tuple = 1,2,3,4,5
print(my_tuple)
print('元组不为空时，里面至少要有一个逗号')
my_tuple = 1,
print(my_tuple) # (1,)
print('==========元组的解包（解构）')
my_tuple = 1,2,3
a, b, c = my_tuple
print(a, c) # 1 3
print('==========交换a,b的值，可以利用元组的解构')
a = 1
b = 3
b, a = a, b
print(a, b) # 3 1
print('==========元组解构时数量不一致')
my_tuple = 1,2,3
print('a, b = my_tuple 执行会报错') # ValueError: too many values to unpack (expected 2)
print('添加星号，获取剩余的元素')
a, *b = my_tuple
print(a, b) # 1 [2, 3]
a, *b, c = 1, 2, 3, 4
print(a, b, c) # 1 [2, 3] 4
*a, b, c = 1, 2, 3, 4
print(a, b, c) # [1, 2] 3 4
print('列表和str也可以解构')
*a, b, c = ['a', 'b', 'c', 'd']
print(a, b, c) # ['a', 'b'] c d
*a, b, c = 'hello word'
print(a, b, c) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o'] r d
# SyntaxError: two starred expressions in assignment
print('*a, *b, c = 1, 2, 3, 4执行报错，不能使用多个*') 
