print('==========集合，只能存储不可变对象，无序，不可重复')
s = {1, 2, 2, 3, 3, 3, 4}
print(s) # {1, 2, 3, 4}
print(type(s)) # <class 'set'>
print('s = {[1,2], [2, 3]}存储可变对象时报错') # TypeError: unhashable type: 'list'
print('==========通过set()将list、str、dict转成set')
print(set([1, 2, 3])) # {1, 2, 3}
print(set('hello')) # {'h', 'o', 'l', 'e'}
print('转换dict时只能将key转换')
print(set({'mes': 'aaa', 'status': 200})) # {'mes', 'status'}
print('==========判断是否存在', 1 in s) # True
print('==========获取长度', len(s)) # 4
print('==========添加')
s = {1, 2, 3}
print(s.add('1')) # None
print(s) # {'1', 1, 2, 3}
print('==========update() 将一个集合中的元素添加到当前集合中')
print(s.update('hello')) # None
print(s) # {1, 2, 3, '1', 'h', 'e', 'l', 'o'}
print('==========update() 可以传递序列或字典作为参数，字典只会使用键')
s.update((1, 'x'))
print(s) # {1, 2, 3, '1', 'o', 'x', 'h', 'e', 'l'}
s.update({'mes': 'xxx', 'status': 200})
print(s) # {1, 2, 3, 'mes', 'l', 'status', 'h', 'o', 'x', 'e', '1'}
print('==========pop() 随机删除并返回集合中的一个元素')
print(s.pop())
print('==========remove() 移除集合中指定的元素')
print(s.remove('mes')) # None
print(s) # {2, 3, 'h', 'e', 'x', 'o', 'status', '1', 'l'}
print('==========clear() 清空集合')
print(s.clear()) # None
print(s) # set()
print('==========copy() 浅复制')
s = {'a', 'b', 'c'}
print(s.copy()) # {'a', 'c', 'b'}

print('==============================集合运算==============================')
s1 = {1, 2}
s2 = {2, 3}
print('交集', s1 & s2) # {2}
print('并集', s1 | s2) # {1, 2, 3}
print('差集', s1 - s2) # {1}
print('异或', s1 ^ s2) # {1, 3}
print('检查s1是s2的子集', s1 <= s2) # False
print({1, 2} <= {1, 2}) # True
print('检查s1是s2的超集', s1 >= s2) # False
print({1, 2} >= {1, 2}) # True
print('检查真子集')
print({1, 2} < {1, 2, 3}) # True
print({1, 2} < {1, 2,}) # False
print('检查真超集。。。')