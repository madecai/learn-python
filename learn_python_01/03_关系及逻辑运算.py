print('==========关系运算')
a = 1
print('比较值相等', a == True) # True
print('比较值和id相等', a is True) # False
print('比较值和id不等', a is not True) # True
print('==========列表比较')
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
print(arr1 == arr2) # True
print(arr1 is arr2) # False
print('==========python中万物皆对象，每个对象都要id')
print(id(1), id(True), id('abc'), id('abc'))
print('比较a在某区间', -1 < a < 10) # True

print('==========取反')
a = 1
print(not a) # False
a = 5
print(not a) # False
print('==========与运算，返回原值')
print(1 and 5) # 5
print(0 and 5) # 0
print('==========或运算，返回原值')
print(1 or 5) # 1
print(0 or 5) # 5
print(0 or False or '' or None) # None