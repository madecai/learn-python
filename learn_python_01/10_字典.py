print('==========创建空字典')
d = {}
print(d) # {}
print(type(d)) # <class 'dict'>

print('==========字典的key可以是任意不可变对象，（int、str、bool、tuple ...），但是一般都用str')
print('这里可以使用缩进')
print('key重复了会被覆盖') 
d = {
    'name': 'xiaoming',
    'name': 'xiaoming1',
    'age': 11
}
print(d) # {'name': 'xiaoming1', 'age': 11}
print('不能像js一样，key如果是str必须用引号，否则会当成一个变量')
# NameError: name 'name' is not defined
# d = {
#     name: 'aaa'
# }
print('==========通过key获取value')
print(d['name'])
print("d['aaaaa'] 不存在会报错") # KeyError: 'aaaaa'
print('==========通过key获取value方式2')
print(d.get('name'))
print('此种方式不存在不会报错', d.get('name111')) # None
print('可以指定一个默认值，不存在返回该值', d.get('name111', 111))
print('==========创建字典方式2，这种方式创建的字典key都是str')
d = dict(name = 'li', age = 11)
print(d) # {'name': 'li', 'age': 11}
print('==========创建字典方式3，双值子序列创建')
# 双值序列，序列中只有两个值，[1,2] ('a',3) 'ab'
# 子序列，如果序列中的元素也是序列，那么我们就称这个元素为子序列
d = dict([['name', 'q'], ['age', 11]])
print(d) # {'name': 'q', 'age': 11}
d = dict([('name', 'w'), ('age', 11)])
print(d) # {'name': 'w', 'age': 11}
d = dict(['ab', 'cd'])
print(d) # {'a': 'b', 'c': 'd'}
print('==========获取长度')
d = {
    'name': 'xiaoming',
    'name': 'xiaoming1',
    'age': 11
}
print(len(d)) # 2
print('==========in, not in检查是否包含key')
print('name' in d) # True
print('name' not in d) # False

print('==========修改字典，key存在则覆盖，不存在则添加')
d = {'message': 'hello'}
d['message'] = 'hello1'
print(d) # {'message': 'hello1'}
d['status'] = 200
print(d) # {'message': 'hello1', 'status': 200}
print('==========添加key-value，存在则不做操作,返回旧value，不存在则添加，返回新value')
d = {'message': 'hello'}
print(d.setdefault('message', 'aaa')) # hello
print(d) # {'message': 'hello'}
print(d.setdefault('status', 500)) # 500
print(d) # {'message': 'hello', 'status': 500}
print('==========删除方式1：del')
d = {'message': 'hello'}
del d['message']
print(d) # {}
print("del d['aaa'] 删除不存报错") # KeyError: 'aaa'
print('==========删除方式2：popitem()')
# popitem()
# 随机删除字典中的一个键值对，一般都会删除最后一个键值对
#   删除之后，它会将删除的key-value作为返回值返回
#   返回的是一个元组，元组中有两个元素，第一个元素是删除的key，第二个是删除的value
d = {}
print('d.popitem()删除空字典报错') # KeyError: 'popitem(): dictionary is empty'
d = {'mes': 'bbbb', 'status': 200}
print(d.popitem()) # ('status', 200)
print(d) # {'mes': 'bbbb'}
print('==========删除方式3：pop()')
d = {'mes': 'bbbb', 'status': 200}
print("d.pop('aaa')删除的key不存在报错") # KeyError: 'aaa'
print('删除的key不存在，给个默认值就不会报错，并且返回默认值', d.pop('aaa', 'xxx'))
print('返回删除的值', d.pop('mes')) # bbbb

print('==========删除方式4(全部清除)：clear()')
d = {'mes': 'bbbb', 'status': 200}
print(d.clear()) # None
print(d) # {}
print('==========浅复制')
d = {'mes': 'bbbb', 'status': 200}
print(d.copy())

print('==========获取keys')
print(d.keys()) # dict_keys(['mes', 'status'])
print(type(d.keys())) # <class 'dict_keys'>
print('==========遍历keys')
for key in d.keys() :
    print(key)

print('==========获取values')
print(d.values()) # dict_values(['bbbb', 200])
print(type(d.values())) # <class 'dict_values'>
print('==========遍历values')
for val in d.values() : 
    print(val)

print('==========获取items')
print(d.items()) # dict_items([('mes', 'bbbb'), ('status', 200)])
print(type(d.items())) # <class 'dict_items'>
print('==========获取key-value')
for k, v in d.items() : 
    print(k, v)
