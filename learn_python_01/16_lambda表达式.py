arr1 = [1, 2, 3, 4, 5]
print('==========================================过滤序列')
r = filter(lambda a : a > 3, arr1)
print(r) # <filter object at 0x0000019ED6D78EB0>
print(type(r)) # <class 'filter'>
print(list(r)) # [4, 5]

print('========================================== map')
r = map(lambda i : i ** 2, arr1) # 平方
print(r) # <map object at 0x000001FA50218FD0>
print(type(r)) # <class 'map'>
print(list(r)) # [1, 4, 9, 16, 25]

print('========================================== reduce，在functools库中，需要导入')
from functools import reduce
r = reduce(lambda x, y : x + y, arr1, 0) # 初始值可以省略
print(r) # 15
print(type(r)) # <class 'int'>

print('========================================== sort')
arr2 = ['bb','aaaa','c','ddddddddd','fff']
arr2.sort(key = len) # 按照长度排序
print(arr2)
arr3 = [2,5,'1',3,'6','4']
arr3.sort(key = int) # 转成int排序
print(arr3)
arr3.sort(key=lambda a : int(a))
print(arr3)

print('========================================== sorted 除了序列还可以排str')
str1 = "2341245721"
print(sorted(str1, key = int)) # ['1', '1', '2', '2', '2', '3', '4', '4', '5', '7']
arr3 = [2,5,'1',3,'6','4']
print(sorted(arr3, key = int)) 
print(sorted(arr3, key=lambda a : int(a)))