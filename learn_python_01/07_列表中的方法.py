print('==========向尾部添加元素')
arr = [0, 1, 2]
print(arr.append('tail')) # None
print(arr) # [0, 1, 2, 'tail']
print('==========向指定位置插入元素')
arr = [0, 1, 2]
print(arr.insert(3, 'tail')) # None
print(arr) # [0, 1, 2, 'tail']
print('==========扩展当前序列')
arr = [0, 1, 2]
arr.extend(['a'])
print(arr) # [0, 1, 2, 'a']
print(id(arr)) 
arr.extend('b')
print(arr) # [0, 1, 2, 'a', 'b']
print(id(arr)) # id不变
arr += 'c'
print(arr) # [0, 1, 2, 'a', 'b', 'c']
print(id(arr)) # id也没变，效果相同
print('==========清空序列')
arr.clear()
print(arr)
print('==========指定位置删除，并返回删除的元素')
arr = ['--0', '--1', '--2']
print(arr.pop(1))
print(arr) # ['--0', '--2']
print('不指定删除最后一个', arr.pop())
print(arr) # ['--0']
print('==========指定位置元素，找到多个只删除第一个')
arr = ['--0', '--0', '--1', '--2']
print(arr.remove('--0')) # None
print(arr) # ['--0', '--1', '--2']
print('==========反转')
print(arr.reverse()) # None
print(arr) # ['--2', '--1', '--0']
print('==========排序')
arr = [11, 2, 5, 7, 3, -2]
print('排序前', arr)
arr.sort()
print('排序后', arr)
arr.sort(reverse = True)
print('倒序', arr)