print('==========列表中可以保存任意的对象')
my_list = [10,'hello',True,None,[1,2,3],print]
print(my_list) # [10, 'hello', True, None, [1, 2, 3], <built-in function print>]
print('==========数组角标越界>>print(my_list[6])') # IndexError: list index out of range
print('==========角标为负数') 
print(my_list[-2])
print('==========获取长度', len(my_list))

print('==========切片，含头不含尾') 
print('从指定位置切到最后', my_list[1:]) # ['hello', True, None, [1, 2, 3], <built-in function print>]
print('从0切到指定位置', my_list[:3]) # [10, 'hello', True]
print('从指定位置切到指定位置', my_list[1:2]) # ['hello']
print('去掉头部和尾部的', my_list[1:-1]) 
print('从头切到尾，相当于copy', my_list[:])
print('和上面结果相同', my_list.copy())
print('==========语法：列表[起始, 结束, 步长]') 
# 步长默认为1，不能为0，可以是负数
print(my_list[0:5:3]) # [10, None]
print(my_list[5:0:-3]) # [<built-in function print>, True]
print(my_list[::-3]) # [<built-in function print>, True]
print(my_list[::-1]) # 相当于倒置数组
print('步长不能为0>>print(my_list[0:5:0])') # ValueError: slice step cannot be zero

print('==========数组拼接') 
arr = [0, 1, 2]
print(arr + [3, 4, 5]) # [0, 1, 2, 3, 4, 5]
print(arr * 3) # [0, 1, 2, 0, 1, 2, 0, 1, 2]
print('==========判断是否存在') 
print(1 in arr) # True
print('1' in arr) # False
print('==========最大值，最小值') 
print(max(arr)) # 2
print(min(arr)) # 0
print('==========获取索引，index()的第二个参数为起始位置，第三个参数终止位置，含头不含尾，没找到抛异常') 
print(arr.index(2))
print(arr.index(2, 0, 3))
print('没找到会抛异常>>arr.index(10)') # ValueError: 10 is not in list
print('==========统计某值出现的次数') 
print([1, 2, 2, '1', 'abc'].count(2)) # 2
print([1, 2, 2, '1', 'abc'].count('1')) # 1
print('==========修改数组') 
updateArr = ['a', 'b', 'c']
print('超过长度报错>> updateArr[3] = "d"') # IndexError: list assignment index out of range
print('==========删除')
del updateArr[2]
print(updateArr) # ['a', 'b']
print('==========使用切片修改')
updateArr = ['a', 'b', 'c']
updateArr[0:1] = [1, 2, 3]
print(updateArr) # [1, 2, 3, 'b', 'c']
print('==========从头部插入')
updateArr[0:0] = ['head']
print(updateArr) # ['head', 1, 2, 3, 'b', 'c']
print('==========设置步长后，序列中元素的个数必须和切片中元素的个数一致')
updateArr[::2] = ['--0', '--2', '--4']
print(updateArr) # ['--0', 1, '--2', 3, '--4', 'c']
# ValueError: attempt to assign sequence of size 3 to extended slice of size 2
print("个数不同报错>>updateArr[::3] = ['--0', '--2', '--4']") 
print('==========通过切片删除元素')
updateArr = [0, 1, 2, 3, 4, 5]
del updateArr[::2]
print(updateArr) # [1, 3, 5]

print('==========以上操作，只适用于可变序列')
s = 'hello'
print(s[1]) # e
# TypeError: 'str' object does not support item assignment
print("不可变序列，无法通过索引来修改>>s[1] = 'a'") 
print('==========可以通过 list() 函数将其他的序列转换为list')
print(list(s)) # ['h', 'e', 'l', 'l', 'o']